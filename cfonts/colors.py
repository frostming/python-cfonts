"""
Utility functions for handling terminal colors
"""
from __future__ import division
import os
from collections import namedtuple

from .consts import ANSI_COLORS, ANSI_RGB

Style = namedtuple("Style", "open,close")


def hex_to_rgb(hex_string):
    """Return a tuple of red, green and blue components for the color
    given as #rrggbb.
    """
    assert len(hex_string) in (4, 7), "Hex color format is not correct."
    if len(hex_string) == 4:
        return tuple(int(c * 2, 16) for c in hex_string[1:])
    return tuple(
        int(hex_string[i:i + 2], 16)
        for i in range(1, len(hex_string), 2)
    )


def rgb_to_hex(rgb):
    return "#" + "".join("%02x" % c for c in rgb)


def rgb_to_hsv(rgb):
    r, g, b = rgb
    r /= 255
    g /= 255
    b /= 255

    max_value = max(r, g, b)
    min_value = min(r, g, b)
    diff = max_value - min_value

    h, s, v = 0, diff / max_value if max_value > 0 else 0, max_value

    if max_value == min_value:
        h = 0
    elif max_value == r:
        h = 60 * (g - b) / diff
        if g < b:
            h += 360
    elif max_value == g:
        h = 60 * (b - r) / diff + 120
    else:
        h = 60 * (r - g) / diff + 240

    return h, (s * 100), (v * 100)


def hsv_to_rgb(hsv):
    h, s, v = hsv
    h /= 60
    s /= 100
    v /= 100
    hi = int(h) % 6

    f = h - int(h)
    p = 255 * v * (1 - s)
    q = 255 * v * (1 - (s * f))
    t = 255 * v * (1 - (s * (1 - f)))
    v *= 255

    result = {
        0: (v, t, p),
        1: (q, v, p),
        2: (p, v, t),
        3: (p, q, v),
        4: (t, p, v),
        5: (v, p, q)
    }[hi]
    return tuple(int(c) for c in result)


def _color_distance(left, right):
    return sum((i - j) ** 2 for i, j in zip(left, right))


def _ensure_rgb(color):
    if color in ANSI_RGB:
        return ANSI_RGB[color]
    return hex_to_rgb(color)


def get_closest(rgb, rgb_map=ANSI_RGB):
    """Return the closest ANSI color name from the given RGB."""
    color = min(rgb_map.items(), key=lambda x: _color_distance(rgb, x[1]))
    return color[0]


def get_linear(start, end, steps):
    """Get a list of numbers interpolated from start to end inclusively."""
    step = (end - start) / (steps - 1)
    return [start + i * step for i in range(steps)]


class AnsiPen:
    """Generate ANSI color styles"""
    CLOSE_BIT = '\x1b[39m'
    BG_CLOSE_BIT = '\x1b[49m'

    def style(self, color, background=False):
        if color == "system":
            return Style("", "")
        if color in ANSI_COLORS:
            return self.ansi_style(color, background)
        elif color.startswith("#"):
            return self.hex_style(color, background)
        raise ValueError("Unsupported color: {}".format(color))

    def ansi_style(self, color, background):
        offset = 10 if background else 0
        close = self.BG_CLOSE_BIT if background else self.CLOSE_BIT
        code = ANSI_COLORS[color]
        return Style("\x1b[{}m".format(offset + code), close)

    def hex_style(self, color, background):
        return self.rgb_style(hex_to_rgb(color), background)

    def rgb_style(self, color, background):
        ansi_color = get_closest(color)
        return self.ansi_style(ansi_color, background)

    def get_gradient(self, colors, steps):
        assert len(colors) >= 2, "At least 2 colors are needed for gradient."
        colors = [_ensure_rgb(color.strip()) for color in colors.split(",")]
        color_steps = [(steps - 1) // (len(colors) - 1)] * (len(colors) - 1)
        if sum(color_steps) < (steps - 1):
            color_steps[-1] += 1
        assert sum(color_steps) == steps - 1
        result = []
        for start, end, st in zip(colors, colors[1:], color_steps):
            start_hsv, end_hsv = rgb_to_hsv(start), rgb_to_hsv(end)
            styles = [
                hsv_to_rgb(hsv)
                for hsv in zip(
                    *[get_linear(s, e, st + 1) for s, e in zip(start_hsv, end_hsv)]
                )
            ]
            assert len(styles) == st + 1
            if result:
                styles.pop(0)
            result.extend(self.rgb_style(c, False) for c in styles)
        return result


class TrueColorPen(AnsiPen):
    def rgb_style(self, color, background):
        open_bit = 48 if background else 38
        close = self.BG_CLOSE_BIT if background else self.CLOSE_BIT
        r, g, b = color
        return Style(
            "\x01\x1b[{};2;{};{};{}m\x02".format(open_bit, r, g, b),
            close
        )


if os.getenv("DISABLE_TRUECOLOR"):
    pen = AnsiPen()
else:
    pen = TrueColorPen()
