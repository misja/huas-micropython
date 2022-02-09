Micropython type hints and additional requirements

## About this package

`huas-micropython` packages [Micropython](https://micropython.org/) stub files, adding [type information](https://www.python.org/dev/peps/pep-0484/) for static type checkers like [MyPi](http://mypy-lang.org/) or [pyright](https://github.com/microsoft/pyright).

IDE's which use these type checkers (e.g. [VSCode](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/)) will in turn be able to provide rich Micropython type hinting, code completion and contextual help to the user, increasing the overall developer experience without the need to install additional pugins.

-   In addition to providing Micropyton type stubs this package adds [adafruit-ampy](https://pypi.org/project/adafruit-ampy/) as an install requirement, see [background](#background) for a rationale.

-   This package intends to be a *transitional* package meaning that at some point in time it will become obsolete depending on community Micropython stub packaging efforts, see [development](#development) for more information.

## Installation<a id="installation"></a>

You can install `huas-micropython` easily from Python's package index. On macOS or Linux, in a terminal run the following command:

```text
 pip3 install --user huas-micropython
```

On Windows, do:

```text
pip install huas-micropython
```

Note on some Linux and macOS systems you might need to run as root with sudo:

```text
sudo pip3 install huas-micropython
```

## Background<a id="background"></a>

This module was created to support students at Hanzehogeschool University of Applied Sciences's bachelor [HBO-ICT](https://www.hanze.nl/nld/onderwijs/techniek/instituut-voor-communicatie-media--it/opleidingen/bachelor/hbo-ict) programme (in Dutch), in particular for students participating in the Internet of Things project.

This package adds [adafruit-ampy](https://pypi.org/project/adafruit-ampy/) as an install requirement to provide all the tooling necessary for working with an [esp32](https://www.espressif.com/en/products/socs/esp32) microcontroller. Note that `adafruit-ampy` is also included in PyCharm's [Micropython plugin](https://plugins.jetbrains.com/plugin/9777-micropython) and as such `huas-micropython` offers *functional parity*.

## Development<a id="development"></a>

Current efforts to maintain Micropython type stubs are at [Josverl/micropython-stubs](https://github.com/Josverl/micropython-stubs) and [hlovatt/PyBoardTypeshed](https://github.com/hlovatt/PyBoardTypeshed). The `huas-micropython` package includes both, using `Josverl/micropython-stubs` for module level stubs and `hlovatt/PyBoardTypeshed` as additional documentation stubs (as a sidenote, PyCharm's [Micropython plugin](https://plugins.jetbrains.com/plugin/9777-micropython) uses `hlovatt/PyBoardTypeshed` stubs).

Two ongoing iniatives are of importance for this package:

-   Integrating and/or combinging work being done at both stub repositories (being discussed at [#98](https://github.com/Josverl/micropython-stubs/issues/98)).

-   Publishing stubs to PyPi, see e.g. [#123](https://github.com/Josverl/micropython-stubs/issues/123) and [#179](https://github.com/vlasovskikh/intellij-micropython/issues/179).

Once the above has been resolved `huas-micropython` will be considered obsolete and retracted from PyPi.
