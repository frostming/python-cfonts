```
  ██████╗ ███████╗  ██████╗  ███╗   ██╗ ████████╗ ███████╗
 ██╔════╝ ██╔════╝ ██╔═══██╗ ████╗  ██║ ╚══██╔══╝ ██╔════╝
 ██║      █████╗   ██║   ██║ ██╔██╗ ██║    ██║    ███████╗
 ██║      ██╔══╝   ██║   ██║ ██║╚██╗██║    ██║    ╚════██║
 ╚██████╗ ██║      ╚██████╔╝ ██║ ╚████║    ██║    ███████║
  ╚═════╝ ╚═╝       ╚═════╝  ╚═╝  ╚═══╝    ╚═╝    ╚══════╝
```
[![Build Status](https://travis-ci.org/frostming/python-cfonts.svg?branch=master)](https://travis-ci.org/frostming/python-cfonts)

*This is a Python port of [cfonts](https://github.com/dominikwilkowski/cfonts). Thanks for the original code and beautiful console fonts!*

> **NOTE:** This project supports Python >= 3.6 ONLY

## Installation

```bash
$ pip3 install python-cfonts
```

## Usage

```bash
$ cfonts --help
Usage: cfonts [OPTIONS] TEXT

  This is a tool for sexy fonts in the console. Give your cli some love.

Options:
  --version                       Show the version and exit.
  -m, --max-length INTEGER        Use to define the amount of maximum
                                  characters per line
  -s, --spaceless                 Use to disable the padding around your
                                  output
  -z, --line-height INTEGER       Use to define your line height
  -l, --letter-spacing INTEGER    Use to define your letter spacing
  -a, --align [left|center|right]
                                  Use to align your text output
  -b, --background [transparent|black|red|green|yellow|blue|magenta|cyan|white|bright_black|bright_red|bright_green|bright_yellow|bright_blue|bright_magenta|bright_cyan|bright_white]
                                  Use to define the background color
  -c, --colors TEXT               Use to define the font color
  -f, --font [console|block|simpleBlock|simple|3d|simple3d|chrome|huge]
                                  Use to define the font face
  --help                          Show this message and exit.
```
![](/images/example.png)

Or generate the fonts pragramatically:

```python
from cfonts import render, say

output = render('Hello world', colors=['red', 'yellow'], align='center')
print(output)
```

## Tests

```bash
$ pipenv run pytest
```

## License

The project is originated by [@dominikwilkowski](https://github.com/dominikwilkowski), under GPLv2 license.
Ported by [@frostming](https://github.com/frostming), under GPLv2 license. See [LICENSE](/LICENSE) for details
