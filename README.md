# Test-driven development for ecology and evolution: Python version

This repository contains a [Python](https://python.org) version of the test-driven development workshop in ecology and evolution, available [here](https://github.com/rscherrer/tdd-workshop) for the R language. It uses the same functions, the same tests and the same bugs, so the practical can be followed in Python.

This documentation provides some requirements and setup instructions. For the actual exercises of the practical, please refer to the documentation in the R version of the workshop, available [here](https://github.com/rscherrer/tdd-workshop). You can also check the solutions there (and corresponding solved code here), if you struggle.

## Prerequisites

For this practical you will need:

* Python (3.12+)

as well as the non-standard libraries (installed with [pip](https://pypi.org/project/pip/) 24.0+):

* [numpy](https://numpy.org/) (2.5.4+)
* [pytest](https://docs.pytest.org/en/stable/) (9.1.1+)
* [pytest-cov](https://pypi.org/project/pytest-cov/) (7.1.0+)

(E.g. `pip install pytest pytest-cov numpy`.)

These libraries can either be installed in the global Python environment or in a virtual environment (after activation). To set up a virtual environment, you may run:

``` bash
python -m venv .venv # you may need to sudo apt install python3-venv on Linux
```

To activate the virtual environment on Windows, run in the command prompt or PowerShell:

``` bash
.venv\Scripts\Activate.ps1
```

or

```bash
.venv\Scripts\activate.bat
```

For Linux or macOS, run in the terminal:

``` bash
source .venv/bin/activate
```

Make sure that any platform-specific requirements on installing software are met (e.g. ticking the "Add python.exe to PATH" checkbox on Windows). As these details are beyond the scope of this tutorial (and we assume some familiarity with Python already), we will not cover them in detail here. 

**Note for VS Code users:** You should make sure that the Python extension is installed and that the correct Python interpreter is selected (e.g. the one from your virtual environment).

The tutorial can be followed in the IDE of your choice (e.g. [VS Code](https://code.visualstudio.com/) with Microsoft's [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)), but can also be run entirely from a command line.

## Setup

Please download this repository. The folder organization is the same as explained in the [R version](https://github.com/rscherrer/tdd-workshop) of the workshop, that is, multiple subfolders, each containing a slightly more complicated code base for a population-genetics toolkit we are trying to build. You will need to set each subfolder as your working directory, in succession, as you go through the exercises (there is one subfolder per exercise).

## Instructions

Find the instructions [here](https://github.com/rscherrer/tdd-workshop).

## Links

* [tdd-workshop](https://github.com/rscherrer/tdd-workshop)
* [tdd-workshop-python](https://github.com/rscherrer/tdd-workshop-python)

## Permissions

Copyright (c) Raphaël Scherrer, 2026.

Snippets of code graciously provided by Koen Freerks.

The code in this repository is shared under the [MIT license](LICENSE.txt) license.
