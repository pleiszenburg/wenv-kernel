[![build_master](https://img.shields.io/travis/pleiszenburg/wenv-kernel/master.svg?style=flat-square "Build Status: master / release")](https://travis-ci.org/pleiszenburg/wenv-kernel)
[![build_develop](https://img.shields.io/travis/pleiszenburg/wenv-kernel/develop.svg?style=flat-square "Build Status: development branch")](https://travis-ci.org/pleiszenburg/wenv-kernel)
[![license](https://img.shields.io/pypi/l/wenvkernel.svg?style=flat-square "GNU Lesser General Public License v2.1")](https://github.com/pleiszenburg/wenv-kernel/blob/master/LICENSE)
[![status](https://img.shields.io/pypi/status/wenvkernel.svg?style=flat-square "Project Development Status")](https://github.com/pleiszenburg/wenv-kernel/issues)
[![pypi_version](https://img.shields.io/pypi/v/wenvkernel.svg?style=flat-square "Project Development Status")](https://pypi.python.org/pypi/wenvkernel)
[![pypi_versions](https://img.shields.io/pypi/pyversions/wenvkernel.svg?style=flat-square "Available on PyPi - the Python Package Index")](https://pypi.python.org/pypi/wenvkernel)

![wenv-kernel](http://www.pleiszenburg.de/wenv-kernel_logo.png)

## Synopsis

**wenv-kernel** is a **Python package** (currently in development **status 4/beta**). It allows to **run Python on top of Wine as a Jupyter kernel** on Linux, MacOS or BSD. It uses **[wenv](https://github.com/pleiszenburg/wenv)**.

## Prerequisites

A working installation of `wenv`, see [installation instructions](https://wenv.readthedocs.io/en/latest/installation.html) in its documentation. If not present, `wenv-kernel` will try to install and configure `wenv` automatically. It is assumed that *Wine* is present.

## Installation

```bash
pip install wenvkernel
python -m wenvkernel.install
```

After installing the package with `pip`, you must not forget to run the kernel install module once as shown above.

## Examples

| launcher | platform | ipc |
|:--------:|:--------:|:---:|
| ![launcher](https://github.com/pleiszenburg/wenv-kernel/blob/master/docs/launcher.png?raw=true "launcher") | ![platform](https://github.com/pleiszenburg/wenv-kernel/blob/master/docs/platform.png?raw=true "platform") | ![ipc](https://github.com/pleiszenburg/wenv-kernel/blob/master/docs/ipc.png?raw=true "ipc") |

See [examples](https://github.com/pleiszenburg/wenv-kernel/blob/master/examples) for example Jupyter notebooks.

## Need help?

Feel free to post questions in the [GitHub issue tracker](https://github.com/pleiszenburg/wenv-kernel/labels/question) of this project.

## Bugs & issues

- Report bugs in *wenv-kernel* here: [wenv-kernel GitHub issue tracker](https://github.com/pleiszenburg/wenv-kernel/issues)
- Report bugs in *wenv* here: [wenv GitHub issue tracker](https://github.com/pleiszenburg/wenv/issues)
- Report bugs in *Wine* here: [WineHQ Bug Tracking System](https://bugs.winehq.org/)

## Miscellaneous

- [Authors](https://github.com/pleiszenburg/wenv-kernel/blob/master/AUTHORS.md)
- [Change log (current)](https://github.com/pleiszenburg/wenv-kernel/blob/develop/CHANGES.md) (changes in development branch since last release)
- [Change log (past)](https://github.com/pleiszenburg/wenv-kernel/blob/master/CHANGES.md) (release history)
- [Contributing](https://github.com/pleiszenburg/wenv-kernel/blob/master/CONTRIBUTING.md) (**Contributions are highly welcomed!**)
- [License](https://github.com/pleiszenburg/wenv-kernel/blob/master/LICENSE) (**LGPL v2.1**)
