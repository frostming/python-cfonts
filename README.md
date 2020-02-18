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

> **NOTE:** This project supports Python 2.7+ and 3.5+

## Installation

```bash
$ pip install python-cfonts
```

## Usage
[Documentation](https://python-cfonts.readthedocs.io/python-cfonts/)

Command line interface:
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
![](https://python-cfonts.readthedocs.io/en/latest/_images/example.png)

Or generate the fonts pragramatically:

```python
from cfonts import render, say

output = render('Hello world', colors=['red', 'yellow'], align='center')
print(output)
```
## Supported Characters

|     |     |     |     |             |
|-----|-----|-----|-----|-------------|
| `A` | `O` | `2` | `2` | `=`         |
| `B` | `P` | `3` | `3` | `@`         |
| `C` | `Q` | `4` | `4` | `#`         |
| `D` | `R` | `5` | `5` | `$`         |
| `E` | `S` | `6` | `6` | `%`         |
| `F` | `T` | `7` | `7` | `&`         |
| `G` | `U` | `8` | `8` | `(`         |
| `H` | `V` | `9` | `9` | `)`         |
| `I` | `W` | `!` | `!` | `/`         |
| `J` | `X` | `?` | `?` | `:`         |
| `K` | `Y` | `.` | `.` | `;`         |
| `L` | `Z` | `+` | `+` | `,`         |
| `M` | `0` | `-` | `-` | `'`         |
| `N` | `1` | `_` | `_` | ` ` (space) |
| `"` |

## Contributing

`python-cfonts` is managed by [pdm](https://github.com/frostming/pdm), first install it:
```bash
pipx install pdm
```
Then, install a dependencies:
```bash
pdm install -d
```
Run tests:
```bash
$ pdm run pytest tests
```

## License

The project is originated by [@dominikwilkowski](https://github.com/dominikwilkowski), under GPLv2 license.
Ported by [@frostming](https://github.com/frostming), under GPLv2 license. See [LICENSE](/LICENSE) for details

## Changelog

- **v0.5.0** Add four new fonts and double quote as supported charater.
- **v0.3.1** Fix a bug that the background doesn't span the full width.
- **v0.3.0** Supports Python 2.7.
- **v0.2.0** Initial commit and testing.
