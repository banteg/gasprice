import click
import pandas as pd
from time import sleep
from threading import Thread
from collections import deque
from statistics import mean
from itertools import chain
from web3 import Web3, HTTPProvider
from sanic import Sanic, response


HOST, PORT = '127.0.0.1', 8000
ETH_RPC_URL = 'http://localhost:8545'
QUANTILES = dict(min=0, low=35, standard=60, fast=90)
WINDOW = 100


w3 = Web3(HTTPProvider(ETH_RPC_URL))
block_times = deque(maxlen=WINDOW)
blocks_gwei = deque(maxlen=WINDOW)
stats = {}


@click.command()
@click.option('--skip-warmup', is_flag=True)
def worker(skip_warmup):
    latest = w3.eth.filter('latest')

    if not skip_warmup:
        warmup()

    while True:
        for n in latest.get_new_entries():
            block = process_block(n)
            print(stats)
        sleep(1)


def warmup():
    tip = w3.eth.blockNumber
    with click.progressbar(range(tip - WINDOW, tip), label='warming up') as bar:
        for n in bar:
            process_block(n)


def block_time():
    if len(block_times) < 2:
        return 0
    times = sorted(block_times)
    avg = mean(b - a for a, b in zip(times, times[1:]))
    stats['block_time'] = round(avg, 2)
    return avg


def process_block(n):
    block = w3.eth.getBlock(n, True)
    stats['block_number'] = block.number

    block_times.append(block.timestamp)
    if len(block_times) > 1:
        t = sorted(block_times)
        stats['block_time'] = round(mean(b - a for a, b in zip(t, t[1:])), 3)

    blocks_gwei.append(min(tx.gasPrice for tx in block.transactions))
    data = pd.Series(blocks_gwei)
    for name, q in QUANTILES.items():
        price = data.quantile(q / 100)
        stats[name] = round(float(w3.fromWei(price, 'gwei')), 3)

    return block


app = Sanic()
app.config.LOGO = ''


@app.route('/')
async def api(request):
    return response.json(stats)


def main():
    bg = Thread(target=worker)
    bg.daemon = True
    bg.start()
    app.run(host=HOST, port=PORT, access_log=False)


if __name__ == '__main__':
    main()
