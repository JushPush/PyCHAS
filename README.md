# PyCHAS
[![Python](https://img.shields.io/pypi/pyversions/PyCHAS.svg?style=for-the-badge&logo=Python)](https://badge.fury.io/py/PyCHAS)
[![PyPI version](https://img.shields.io/pypi/v/PyCHAS?style=for-the-badge&logo=PyPi)](https://badge.fury.io/py/PyCHAS)
[![](https://img.shields.io/pypi/dd/PyCHAS?style=for-the-badge&logo=PyPi&label=Downloads@PyPi&color=blue)](https://badge.fury.io/py/PyCHAS)

[![Upload Python Package](https://img.shields.io/github/actions/workflow/status/EinKara/PyCHAS/python-publish.yml?label=Publish&logo=PyPi&logoColor=green&style=for-the-badge)](https://github.com/EinKara/PyCHAS/actions/workflows/python-publish.yml) 
[![Python package](https://img.shields.io/github/actions/workflow/status/EinKara/PyCHAS/python-package.yml?logo=Github&style=for-the-badge)](https://github.com/EinKara/PyCHAS/actions/workflows/python-package.yml)
[![Checks](https://img.shields.io/github/checks-status/EinKara/PyCHAS/main?style=for-the-badge&logo=Git)](https://badge.fury.io/py/PyCHAS)
[![Issues](https://img.shields.io/github/issues/EinKara/PyCHAS?logo=Github&style=for-the-badge)](https://github.com/EinKara/PyCHAS/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/EinKara/PyCHAS?logo=Github&style=for-the-badge)](https://github.com/EinKara/PyCHAS/pulls)
[![License](https://img.shields.io/pypi/l/PyCHAS?style=for-the-badge)](https://github.com/EinKara/PyCHAS)

[![Sponsors](https://img.shields.io/github/sponsors/EinKara?style=for-the-badge&logo=Github)](https://github.com/sponsors/EinKara/)

---

PyCHAS ( Python C/C++ header amalgamation script ) is a tool for compiling C/C++ headers into one; allowing for better organization.

## Usage

A header starting header file is required. The script goes through all included local headers, and puts external includes at the top of the output header.

The script also utilizes the "#pragma" for settings.

```cpp
#pragma PYCHAS path . // Current file path
#pragma PYCHAS comments off // On/Off
#pragma PYCHAS noexpand // Don't expand included headers
```

And for usage

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

---

[![Github](https://img.shields.io/github/followers/EinKara?logo=Github&style=for-the-badge)](https://github.com/EinKara)
[![Twitter](https://img.shields.io/twitter/follow/notokay3272?color=lightblue&logo=twitter&style=for-the-badge&label=Follow)](https://www.twitter.com/notokay3272/)
