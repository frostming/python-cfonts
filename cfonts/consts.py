"""
    Python cFonts
    =============
    Sexy fonts for the console.

    :license: GNU GPLv2
    :author: Frost Ming<mianghong@gmail.com>
"""
import enum
from shutil import get_terminal_size
from typing import Mapping, Tuple

SIZE = get_terminal_size((80, 24))
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|!?.+-_=@#$%&()/:;,' \""


class Colors(enum.Enum):
    system = "system"
    black = "black"
    red = "red"
    green = "green"
    yellow = "yellow"
    blue = "blue"
    magenta = "magenta"
    cyan = "cyan"
    white = "white"
    candy = "candy"
    bright_red = "bright_red"
    bright_green = "bright_green"
    bright_yellow = "bright_yellow"
    bright_blue = "bright_blue"
    bright_magenta = "bright_magenta"
    bright_cyan = "bright_cyan"
    bright_white = "bright_white"


class CandyColors(enum.Enum):
    red = "red"
    green = "green"
    yellow = "yellow"
    blue = "blue"
    magenta = "magenta"
    cyan = "cyan"
    gray = "gray"
    bright_red = "bright_red"
    bright_green = "bright_green"
    bright_yellow = "bright_yellow"
    bright_blue = "bright_blue"
    bright_magenta = "bright_magenta"
    bright_cyan = "bright_cyan"


class BgColors(enum.Enum):
    transparent = "transparent"
    black = "black"
    red = "red"
    green = "green"
    yellow = "yellow"
    blue = "blue"
    magenta = "magenta"
    cyan = "cyan"
    white = "white"
    bright_black = "bright_black"
    bright_red = "bright_red"
    bright_green = "bright_green"
    bright_yellow = "bright_yellow"
    bright_blue = "bright_blue"
    bright_magenta = "bright_magenta"
    bright_cyan = "bright_cyan"
    bright_white = "bright_white"


ALIGNMENT = ["left", "center", "right"]


class FontFaces(enum.Enum):
    console = "console"
    block = "block"
    simpleblock = "simpleBlock"
    simple = "simple"
    threed = "3d"
    simple3d = "simple3d"
    chrome = "chrome"
    huge = "huge"
    grid = "grid"
    pallet = "pallet"
    shade = "shade"
    slick = "slick"
    tiny = "tiny"


ANSI_COLORS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
    "gray": 90,
    "bright_red": 91,
    "bright_green": 92,
    "bright_yellow": 93,
    "bright_blue": 94,
    "bright_magenta": 95,
    "bright_cyan": 96,
    "bright_white": 97,
}

ANSI_RGB: Mapping[str, Tuple[int, int, int]] = {
    "black": (0, 0, 0),
    "red": (127, 0, 0),
    "green": (0, 127, 0),
    "yellow": (127, 127, 0),
    "blue": (0, 0, 127),
    "magenta": (127, 0, 127),
    "cyan": (0, 127, 127),
    "white": (127, 127, 127),
    "gray": (64, 64, 64),
    "bright_red": (255, 0, 0),
    "bright_green": (0, 255, 0),
    "bright_yellow": (255, 255, 0),
    "bright_blue": (0, 0, 255),
    "bright_magenta": (255, 0, 255),
    "bright_cyan": (0, 255, 255),
    "bright_white": (255, 255, 255),
}
