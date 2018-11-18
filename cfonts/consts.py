"""
    Python cFonts
    =============
    Sexy fonts for the console.

    :license: GNU GPLv2
    :author: Frost Ming<mianghong@gmail.com>
"""
try:
    from shutil import get_terminal_size
except ImportError:
    from backports.shutil_get_terminal_size import get_terminal_size

SIZE = tuple(get_terminal_size((80, 24)))
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|!?.+-_=@#$%&()/:;,' "


class Enum:
    @classmethod
    def all(cls):
        return [
            v for k, v in cls.__dict__.items() if not k.startswith("_") and k != "all"
        ]


class COLORS(Enum):
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


class CANDYCOLORS(Enum):
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


class BGCOLORS(Enum):
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


class FONTFACES(Enum):
    console = "console"
    block = "block"
    simpleblock = "simpleBlock"
    simple = "simple"
    threed = "3d"
    simple3d = "simple3d"
    chrome = "chrome"
    huge = "huge"


ANSI_COLORS = {
    "black": [30, 39],
    "red": [31, 39],
    "green": [32, 39],
    "yellow": [33, 39],
    "blue": [34, 39],
    "magenta": [35, 39],
    "cyan": [36, 39],
    "white": [37, 39],
    "gray": [90, 39],
    "bright_red": [91, 39],
    "bright_green": [92, 39],
    "bright_yellow": [93, 39],
    "bright_blue": [94, 39],
    "bright_magenta": [95, 39],
    "bright_cyan": [96, 39],
    "bright_white": [97, 39],
}
