# gasprice

estimates ethereum gas price based on recent blocks and provides a simple api

## installation

requires python 3.6 and an ethereum full node. you can use infura.io as well.

```bash
pip install gasprice
```

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
  "low": 1,
  "standard": 4,
  "fast": 20,
}
```
