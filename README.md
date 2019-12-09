[![build_master](https://img.shields.io/travis/pleiszenburg/wenv-kernel/master.svg?style=flat-square "Build Status: master / release")](https://travis-ci.org/pleiszenburg/wenv-kernel)
[![docs_master](https://readthedocs.org/projects/wenv-kernel/badge/?version=latest&style=flat-square "Documentation Status: master / release")](https://wenv-kernel.readthedocs.io/en/latest/)
[![build_develop](https://img.shields.io/travis/pleiszenburg/wenv-kernel/develop.svg?style=flat-square "Build Status: development branch")](https://travis-ci.org/pleiszenburg/wenv-kernel)
[![docs_develop](https://readthedocs.org/projects/wenv-kernel/badge/?version=develop&style=flat-square "Documentation Status: development branch")](https://wenv-kernel.readthedocs.io/en/develop/)
[![license](https://img.shields.io/pypi/l/wenvkernel.svg?style=flat-square "Internet Systems Consortium License")](https://github.com/pleiszenburg/wenv-kernel/blob/master/LICENSE)
[![status](https://img.shields.io/pypi/status/wenvkernel.svg?style=flat-square "Project Development Status")](https://github.com/pleiszenburg/wenv-kernel/issues)
[![pypi_version](https://img.shields.io/pypi/v/wenvkernel.svg?style=flat-square "Project Development Status")](https://pypi.python.org/pypi/wenvkernel)
[![pypi_versions](https://img.shields.io/pypi/pyversions/wenvkernel.svg?style=flat-square "Available on PyPi - the Python Package Index")](https://pypi.python.org/pypi/wenvkernel)

![wenv](http://www.pleiszenburg.de/wenv-kernel_logo.png)

## Synopsis

**wenv-kernel** is a **Python package** (currently in development **status 4/beta**). It allows to **run Python on top of Wine as a Jupyter kernel** on Linux, MacOS or BSD. It is based upon **[wenv](https://github.com/pleiszenburg/wenv)**.

## Prerequisites

A working installation of `wenv`, see [installation instructions](https://wenv.readthedocs.io/en/latest/installation.html) in its documentation. If not present, `wenv-kernel` will try to install and configure `wenv` automatically. It is assumed that *Wine* is present.

## Installation

| branch | status | installation | documentation |
| --- | --- | --- | --- |
| master (release) | [![build_master](https://img.shields.io/travis/pleiszenburg/wenv-kernel/master.svg?style=flat-square "Build Status: master / release")](https://github.com/pleiszenburg/wenv-kernel/blob/master/LICENSE) | `pip install wenvkernel` | [![docs_master](https://readthedocs.org/projects/wenv/-kernelbadge/?version=latest&style=flat-square "Documentation Status: master / release")](https://wenv-kernel.readthedocs.io/en/latest/) |
| develop | [![build_develop](https://img.shields.io/travis/pleiszenburg/wenv-kernel/develop.svg?style=flat-square "Build Status: development branch")](https://wenv-kernel.readthedocs.io/en/develop/) | `pip install git+https://github.com/pleiszenburg/wenv-kernel.git@develop` | [![docs_develop](https://readthedocs.org/projects/wenv-kernel/badge/?version=develop&style=flat-square "Documentation Status: development branch")](https://github.com/pleiszenburg/wenv-kernel/blob/master/LICENSE) |

After installing the package with `pip`, you must initialize the "Wine Python environment" by running ``wenv init``.

## Examples

[TBD]

## Need help?

Feel free to post questions in the [GitHub issue tracker](https://github.com/pleiszenburg/wenv-kernel/labels/question) of this project.

## Bugs & issues

- Report bugs in *wenv-kernel* here: [wenv-kernel GitHub issue tracker](https://github.com/pleiszenburg/wenv-kernel/issues)
- Report bugs in *wenv* here: [wenv GitHub issue tracker](https://github.com/pleiszenburg/wenv/issues)
- Report bugs in *Wine* here: [WineHQ Bug Tracking System](https://bugs.winehq.org/)

## Miscellaneous

- Full project documentation
    - at [Read the Docs](http://wenv-kernel.readthedocs.io/en/latest/)
    - at [`wenv-kernel` repository](https://github.com/pleiszenburg/wenv-kernel/blob/master/docs/index.rst)
- [Authors](https://github.com/pleiszenburg/wenv-kernel/blob/master/AUTHORS.md)
- [Change log (current)](https://github.com/pleiszenburg/wenv-kernel/blob/develop/CHANGES.md) (changes in development branch since last release)
- [Change log (past)](https://github.com/pleiszenburg/wenv-kernel/blob/master/CHANGES.md) (release history)
- [Contributing](https://github.com/pleiszenburg/wenv-kernel/blob/master/CONTRIBUTING.md) (**Contributions are highly welcomed!**)
- [FAQ](http://wenv-kernel.readthedocs.io/en/stable/faq.html)
- [License](https://github.com/pleiszenburg/wenv-kernel/blob/master/LICENSE) (**LGPL v2.1**)
- [Upstream issues](https://github.com/pleiszenburg/wenv-kernel/issues?q=is%3Aissue+is%3Aopen+label%3Aupstream) (relevant bugs in dependencies)
