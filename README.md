# Detawane

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE) [![CI](https://github.com/slow-query/detawane/workflows/CI/badge.svg)](https://github.com/slow-query/detawane/actions?query=workflow%3ACI)

Detawane is application that notify twitter when channel owner post message on live chat (for 2434 free chat).

## Development

### Setup

```shell
pip install -r requirements.txt
cp .envrc.sample .envrc
```

For increase the efficiency of development.

```shell
pip install pre-commit
pre-commit install
```

### Run

```shell
python -m detawane --file ./your/file/path
```

## Great thanks

[taizan-hokuto/pytchat](https://github.com/taizan-hokuto/pytchat)
