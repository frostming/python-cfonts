"""
    Python cFonts
    =============
    Sexy fonts for the console.

    :license: GNU GPLv2
    :author: Frost Ming<mianghong@gmail.com>
"""
import json
import random
import re
from pathlib import Path
from typing import List, Tuple, Union

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
CharArray = List[str]
SizeTuple = Tuple[int, ...]
LetterSpacing = Union[int, None]

ansi_styles = {"system": ("", "")}
for k, v in ANSI_COLORS.items():
    ansi_styles[k] = (f"\x1b[{v[0]}m", f"\x1b[{v[1]}m")
    ansi_styles["bg" + k] = (f"\x1b[{v[0] + 10}m", f"\x1b[{v[1] + 10}m")


class Font:

    def __init__(self, name: str) -> None:
        self.name = name
        if name == FONTFACES.console:
            self.colors = 1
            self.lines = 1
            return
        font_file = (Path(__file__) / f"../fonts/{name}.json").resolve()
        font_face = json.loads(font_file.read_text("utf-8"))
        self.__dict__.update(font_face)

    def add_letter_spacing(
        self, output: CharArray, colors: CharArray, letter_spacing: int
    ) -> CharArray:
        lines = len(output) - self.lines
        for i in range(lines, len(output)):
            idx = i - lines
            space = colorize(self.letterspace[idx], self.colors, colors) or " "
            output[i] += space * letter_spacing
        return output

    def add_char(self, output: CharArray, char: str, colors: CharArray) -> CharArray:
        lines = len(output) - self.lines
        for i in range(lines, len(output)):
            idx = i - lines
            output[i] += colorize(self.chars[char][idx], self.colors, colors)
        return output


def add_line(output: CharArray, buffer: CharArray, line_height: int) -> CharArray:
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


def get_font(font: str) -> Font:
    """Get a selected JSON font-file object.

    :param font: The name of the font to be returned
    :returns: The font object of that file
    :raises: FileNotFoundError
    """
    return Font(font)


def clean_input(text: str, allowed_chars: str = CHARS) -> str:
    """Filter only allowed characters.

    :param text: The input text to be filtered
    :param allowed_chars: Allowed characters
    :returns: The filtered input text
    """
    return "".join(c for c in text if c.upper() in allowed_chars)


def char_length(character: CharArray, letter_spacing: int = 0) -> int:
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


def align_text(
    output: CharArray,
    line_length: int,
    character_lines: int,
    align: str,
    size: SizeTuple = SIZE,
) -> CharArray:
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


def colorize(character: str, font_colors: int, colors: CharArray) -> str:
    if font_colors > 1:
        for i in range(font_colors):
            try:
                color = colors[i]
            except IndexError:
                color = COLORS.system
            if color == COLORS.candy:
                color = random.choice(CANDYCOLORS.all())

            character = re.sub(f"<c{i + 1}>", ansi_styles[color][0], character)
            character = re.sub(f"</c{i + 1}>", ansi_styles[color][1], character)
    elif font_colors == 1:
        try:
            color = colors[0]
        except IndexError:
            color = COLORS.system
        if color == COLORS.candy:
            color = random.choice(CANDYCOLORS.all())
        character = ansi_styles[color][0] + re.sub(
            r"(<([^>]+)>)", "", character
        ) + ansi_styles[
            color
        ][
            1
        ]
    return character


def render_console(
    text: str,
    *,
    size: SizeTuple = SIZE,
    colors: CharArray = [],
    align: str = "left",
    letter_spacing: LetterSpacing = None,
    line_height: int = 1,
) -> CharArray:
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
            output_lines[i:i + 1] = line[:size[0]].strip(), line[size[0]:].strip()
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
    text: str,
    *,
    font: str = FONTFACES.block,
    size: SizeTuple = SIZE,
    colors: CharArray = [],
    background: str = BGCOLORS.transparent,
    align: str = "left",
    letter_spacing: LetterSpacing = None,
    line_height: int = 1,
    space: bool = True,
    max_length: int = 0,
) -> str:
    output = []  # type: CharArray
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

    write = "\n".join(output)
    if font_face.colors <= 1:
        write = colorize(write, font_face.colors, colors)
    if space:
        write = f"\n\n{write}\n\n"
    if background != BGCOLORS.transparent:
        bg_color = "bg" + background
        write = ansi_styles[bg_color][0] + "\n" + write + ansi_styles[bg_color][1]

    return write


def say(text: str, **options):
    write = render(text, **options)
    if write:
        click.echo(write)
