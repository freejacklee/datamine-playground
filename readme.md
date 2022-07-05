# Datamine Playground

## introduction

Here are my private projects relative to web-crawl/reverse individually but sharing the some environment.

May you have fun.

## project list

- `project_deepl`: an api of calling deepl translation, based on javascript reverse analysis

## installation (fully based on python 3+, 3.9 is better)

### fastest way

```shell
pip install -r requirements.txt
```

### better way in case of polluting the global python environment

```shell
pip install virtualenv
virtualenv venv
source venv/bin/python
```

## usage

I make all the scripts based on `argparse`, so that you can use `python xxx.py -h` to see the manual of each project.

take the `project_deepl` as an example:

```shell
cd project_deepl
python main.py -h
```