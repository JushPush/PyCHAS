# PyCHAS
[![Python](https://img.shields.io/pypi/pyversions/PyCHAS.svg?style=for-the-badge)](https://badge.fury.io/py/PyCHAS)
[![PyPI version](https://badge.fury.io/py/PyCHAS.svg?style=for-the-badge)](https://badge.fury.io/py/PyCHAS)


[![Upload Python Package](https://github.com/EinKara/PyCHAS/actions/workflows/python-publish.yml/badge.svg)](https://github.com/EinKara/PyCHAS/actions/workflows/python-publish.yml) [![Python package](https://img.shields.io/github/actions/workflow/status/EinKara/PyCHAS/python-package.yml?style=for-the-badge)](https://github.com/EinKara/PyCHAS/actions/workflows/python-package.yml)

Python C/C++ header amalgamation script

## Usage

```console
$ pychas -h
usage: pychas [-h] [-o OUTPUT] [--debug] file

Creates single-header libraries from given top-level input
file.

positional arguments:
  file                  top-level file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file or directory
  --debug               verbose debug output

If output exists and is a directory, the file is saved
inside with the same name as the input.
```
