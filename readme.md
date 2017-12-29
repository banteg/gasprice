# gasprice

estimates ethereum gas price based on recent blocks and provides a simple api

## hosted

- https://gasprice.poa.network (kindly deployed by [poa network](https://poa.network))

## installation

requires python 3.6 and an ethereum full node. infura.io won't work as it doesn't allow setting up `filter`.

```bash
pip install gasprice
```

there is an example of systemd service if you want to run it as a service.

## usage

```bash
gasprice

Options:
  -h, --host 127.0.0.1
  -p, --port 8000
  -s, --skip-warmup
```

ethereum rpc url can be set with `ETH_RPC_URL` environment variable (default `http://localhost:8545`).

## api

```json
{
  "block_number": 4813900,
  "block_time": 14.9,
  "health": true,
  "slow": 1,
  "standard": 4,
  "fast": 20,
  "instant": 40
}
```

`slow`, `standard`, `fast` and `instant` values represent minimal gas price of the latest 200 blocks. by default slow represents 30% probability, standard is 60%, fast is 90% and instant is 100%.
