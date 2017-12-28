# gasprice

estimates ethereum gas price based on recent blocks and provides a simple api

## installation

requires python 3.6 and ethereum full node. you can use infura.io as well.

```shell
pip install gasprice
```

## usage

```bash
gasprice
gasprice --no-warmup  # to skip loading recent blocks

http localhost:8000
```

