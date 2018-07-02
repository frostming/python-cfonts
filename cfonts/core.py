"""
    Python cFonts
    =============
    Sexy fonts for the console.

    :license: GNU GPLv2
    :author: Frost Ming<mianghong@gmail.com>
"""
from __future__ import unicode_literals
import json
import os
import random
import re

import colorama
import click
from .consts import (
    CHARS,
    BGCOLORS,
    FONTFACES,
    COLORS,
    SIZE,
    CANDYCOLORS,
    ANSI_COLORS,
    ALIGNMENT,
)

colorama.init()
ansi_styles = {"system": ("", "")}
for k, v in ANSI_COLORS.items():
    ansi_styles[k] = ("\x1b[{}m".format(v[0]), "\x1b[{}m".format(v[1]))
    ansi_styles["bg" + k] = ("\x1b[{}m".format(v[0] + 10), "\x1b[{}m".format(v[1] + 10))


class Font:
    def __init__(self, name):
        self.name = name
        if name == FONTFACES.console:
            self.colors = 1
            self.lines = 1
            return
        font_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "fonts/{}.json".format(name))
        )
        font_face = json.loads(open(font_file, "rb").read().decode("utf-8"))
        self.__dict__.update(font_face)

    def add_letter_spacing(self, output, colors, letter_spacing):
        lines = len(output) - self.lines
        for i in range(lines, len(output)):
            idx = i - lines
            space = colorize(self.letterspace[idx], self.colors, colors) or " "
            output[i] += space * letter_spacing
        return output

    def add_char(self, output, char, colors):
        lines = len(output) - self.lines
        for i in range(lines, len(output)):
            idx = i - lines
            output[i] += colorize(self.chars[char][idx], self.colors, colors)
        return output


def add_line(output, buffer, line_height):
    """Add a new line to the output array.

    :param output: The output array the line shall be appended to
    :param buffer: An array of space we add at the beginning of each line
    :param line_height: The user defined line height

    :returns: The output array with new line
    """
    if not output:
        line_height = 0
    for _ in range(line_height):
        output.append("")
    output.extend(buffer)
    return output


def get_font(font):
    """Get a selected JSON font-file object.

    :param font: The name of the font to be returned
    :returns: The font object of that file
    :raises: FileNotFoundError
    """
    return Font(font)


def clean_input(text, allowed_chars=CHARS):
    """Filter only allowed characters.

    :param text: The input text to be filtered
    :param allowed_chars: Allowed characters
    :returns: The filtered input text
    """
    return "".join(c for c in text if c.upper() in allowed_chars)


def char_length(character, letter_spacing=0):
    """Return the max width of a character by looking at its longest line.

    :param character: The character array from the font face
    :param letter_spacing: The user defined letter spacing
    :returns: The length of a longest line in a character
    """
    stripped = [re.sub(r"(<([^>]+)>)", "", char) for char in character]
    char_width = max(map(len, stripped))

    if char_width == 0 and letter_spacing > 0:
        # Adding space to letter spacing
        char_width = 1
    return char_width


def align_text(output, line_length, character_lines, align, size=SIZE):
    assert align in ALIGNMENT
    space = 0
    if align == "center":
        space = (size[0] - line_length) // 2
    elif align == "right":
        space = size[0] - line_length
    if space > 0:
        lines = len(output) - character_lines
        for i in range(lines, len(output)):
            output[i] = " " * space + output[i]
    return output


def colorize(character, font_colors, colors):
    if font_colors > 1:
        for i in range(font_colors):
            try:
                color = colors[i]
            except IndexError:
                color = COLORS.system
            if color == COLORS.candy:
                color = random.choice(CANDYCOLORS.all())

            character = re.sub("<c{}>".format(i + 1), ansi_styles[color][0], character)
            character = re.sub("</c{}>".format(i + 1), ansi_styles[color][1], character)
    elif font_colors == 1:
        try:
            color = colors[0]
        except IndexError:
            color = COLORS.system
        if color == COLORS.candy:
            color = random.choice(CANDYCOLORS.all())
        character = (
            ansi_styles[color][0]
            + re.sub(r"(<([^>]+)>)", "", character)
            + ansi_styles[color][1]
        )
    return character


def render_console(
    text, size=SIZE, colors=[], align="left", letter_spacing=None, line_height=1
):
    output = []
    i = 0
    letter_spacing = max((letter_spacing or 1) - 1, 0)
    line_height = max(line_height - 1, 0)
    space = " " * letter_spacing
    LINE_BREAK_RE = re.compile(r"\r\n|\r|\n|\|")
    output_lines = [
        space.join(list(line)) for line in LINE_BREAK_RE.split(text.strip())
    ]

    while i < len(output_lines):
        line = output_lines[i]
        if len(line) > size[0]:
            output_lines[i : i + 1] = line[: size[0]].strip(), line[size[0] :].strip()
            line = output_lines[i]
        if len(colors) > 0 and colors[0] == COLORS.candy:
            output.append("".join(colorize(c, 1, colors) for c in line))
        else:
            output.append(line)

        output = align_text(output, len(line), 1, align, size)
        output = add_line(output, [], line_height)

        i += 1

    return output


def render(
    text,
    font=FONTFACES.block,
    size=SIZE,
    colors=[],
    background=BGCOLORS.transparent,
    align="left",
    letter_spacing=None,
    line_height=1,
    space=True,
    max_length=0,
):
    """Main function to get the colored output for a string.

    :param text: the string you want to render
    :param font: use to define the font
    :param size: a (width, height) tuple to define the window size
    :param colors: a list of color names to render sequentially
    :param background: background color name
    :param align: the alignment method: left/center/right
    :param letter_spacing: the amount of spacing inserted between letters
    :param line_height: the height of each line
    :param space: whether to wrap the output with blank lines
    :param max_length: define the max length of per line, use 0 to disable
    :returns: the colored output string
    """
    output = []
    lines = 0
    font_face = get_font(font)
    if font == FONTFACES.console:
        # console fontface is pretty easy to process
        output = render_console(
            text,
            size=size,
            colors=colors,
            align=align,
            letter_spacing=letter_spacing,
            line_height=line_height,
        )
        lines = len(output)
    else:
        if letter_spacing is None:
            letter_spacing = char_length(font_face.letterspace)
        line_length = char_length(font_face.buffer)
        max_chars = 0
        output = add_line([], font_face.buffer, line_height)
        lines += 1
        output = font_face.add_letter_spacing(output, colors, letter_spacing)
        line_length += (
            char_length(font_face.letterspace, letter_spacing) * letter_spacing
        )
        text = clean_input(text)
        for c in text:
            c = c.upper()
            last_line_length = line_length

            if c != "|":
                line_length += char_length(font_face.chars[c], letter_spacing)
                line_length += (
                    char_length(font_face.letterspace, letter_spacing) * letter_spacing
                )

            if (
                max_chars > max_length
                and max_length != 0
                or c == "|"
                or line_length > size[0]
            ):
                lines += 1
                output = align_text(
                    output, last_line_length, font_face.lines, align, size
                )

                line_length = char_length(font_face.buffer)
                line_length += (
                    char_length(font_face.letterspace, letter_spacing) * letter_spacing
                )
                if c != "|":
                    # if this is a character and not a line break
                    line_length += char_length(font_face.chars[c], letter_spacing)
                    line_length += (
                        char_length(font_face.letterspace, letter_spacing)
                        * letter_spacing
                    )
                max_chars = 0
                output = add_line(output, font_face.buffer, line_height)
                output = font_face.add_letter_spacing(output, colors, letter_spacing)

            if c != "|":
                output = font_face.add_char(output, c, colors)
                output = font_face.add_letter_spacing(output, colors, letter_spacing)

        output = align_text(output, line_length, font_face.lines, align, size)

    if space:
        # Blank lines at the beginning and end
        output = [""] * 2 + output + [""] * 2
    if background != BGCOLORS.transparent:
        # Fill whitespaces to the full width.
        # See https://github.com/frostming/python-cfonts/issues/3
        output = [(line + " " * (size[0] - len(_strip_color(line)))) for line in output]
        bg_color = "bg" + background
        if output:
            output[0] = ansi_styles[bg_color][0] + output[0]
            output[-1] += ansi_styles[bg_color][1]
    write = "\n".join(output)
    if font_face.colors <= 1:
        write = colorize(write, font_face.colors, colors)

    return write


def say(text, **options):
    """Render and write the output to stout.

    :param text: the string you want to render
    :param \**options: options passed as same as :func:`cfonts.render`
    :returns: None
    """
    write = render(text, **options)
    if write:
        click.echo(write)


def _strip_color(text):
    REGEX = re.compile(r'\x1b\[\d+?m')
    return REGEX.sub('', text)
