```
  ██████╗ ███████╗  ██████╗  ███╗   ██╗ ████████╗ ███████╗
 ██╔════╝ ██╔════╝ ██╔═══██╗ ████╗  ██║ ╚══██╔══╝ ██╔════╝
 ██║      █████╗   ██║   ██║ ██╔██╗ ██║    ██║    ███████╗
 ██║      ██╔══╝   ██║   ██║ ██║╚██╗██║    ██║    ╚════██║
 ╚██████╗ ██║      ╚██████╔╝ ██║ ╚████║    ██║    ███████║
  ╚═════╝ ╚═╝       ╚═════╝  ╚═╝  ╚═══╝    ╚═╝    ╚══════╝
```

![Tests](https://github.com/frostming/python-cfonts/workflows/Tests/badge.svg)

_This is a Python port of [cfonts](https://github.com/dominikwilkowski/cfonts). Thanks for the original code and beautiful console fonts!_

> **NOTE:** This project supports Python 2.7+ and 3.5+

## Installation

```bash
$ pip install python-cfonts
```

## Usage

[Documentation](https://python-cfonts.fming.dev/)

Command line interface:

```bash
usage: cfonts [-h] [-V]
              [-f {console,block,simpleBlock,simple,3d,simple3d,chrome,huge,grid,pallet,shade,slick}]
              [-c COLORS] [-b BACKGROUND] [-a {left,center,right}]
              [-l LETTER_SPACING] [-z LINE_HEIGHT] [-s] [-m MAX_LENGTH]
              [-g GRADIENT] [-i] [-t]
              text

positional arguments:
  text

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -f {console,block,simpleBlock,simple,3d,simple3d,chrome,huge,grid,pallet,shade,slick}, --font {console,block,simpleBlock,simple,3d,simple3d,chrome,huge,grid,pallet,shade,slick}
                        Use to define the font face
  -c COLORS, --colors COLORS
                        Use to define the font color
  -b BACKGROUND, --background BACKGROUND
                        Use to define the background color
  -a {left,center,right}, --align {left,center,right}
                        Use to align the text output
  -l LETTER_SPACING, --letter-spacing LETTER_SPACING
                        Use to define the letter spacing
  -z LINE_HEIGHT, --line-height LINE_HEIGHT
                        Use to define the line height
  -s, --spaceless       Use to define the background color
  -m MAX_LENGTH, --max-length MAX_LENGTH
                        Use to define the amount of maximum characters per
                        line
  -g GRADIENT, --gradient GRADIENT
                        Define gradient colors(separated by comma)
  -i, --independent-gradient
                        Set this option to re-calculate the gradient colors
                        for each new line.Only works in combination with the
                        gradient option.
  -t, --transition-gradient
                        Set this option to generate your own gradients. Each
                        color set in the gradient option will then be
                        transitioned to directly.
```

![](https://python-cfonts.fming.dev/_images/example.png)

Or generate the fonts pragramatically:

```python
from cfonts import render, say

output = render('Hello world', colors=['red', 'yellow'], align='center')
print(output)
```

## Supported Characters

|     |     |     |     |            |
| --- | --- | --- | --- | ---------- |
| `A` | `O` | `2` | `2` | `=`        |
| `B` | `P` | `3` | `3` | `@`        |
| `C` | `Q` | `4` | `4` | `#`        |
| `D` | `R` | `5` | `5` | `$`        |
| `E` | `S` | `6` | `6` | `%`        |
| `F` | `T` | `7` | `7` | `&`        |
| `G` | `U` | `8` | `8` | `(`        |
| `H` | `V` | `9` | `9` | `)`        |
| `I` | `W` | `!` | `!` | `/`        |
| `J` | `X` | `?` | `?` | `:`        |
| `K` | `Y` | `.` | `.` | `;`        |
| `L` | `Z` | `+` | `+` | `,`        |
| `M` | `0` | `-` | `-` | `'`        |
| `N` | `1` | `_` | `_` | `` (space) |
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
Ported by [@frostming](https://github.com/frostming), under MIT license. See [LICENSE](/LICENSE) for details

## Changelog

- **v1.3.0** Relicense to MIT.
- **v1.2.0** Add font `tiny`.
- **v1.1.0** Switch to `argparse` to drop dependency `click`.
- **v1.0.0** Support gradient colors and transition gradient.
- **v0.5.0** Add four new fonts and double quote as supported charater.
- **v0.3.1** Fix a bug that the background doesn't span the full width.
- **v0.3.0** Supports Python 2.7.
- **v0.2.0** Initial commit and testing.
