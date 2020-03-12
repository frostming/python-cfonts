"""
    Python cFonts
    =============
    Sexy fonts for the console.

    :license: GNU GPLv2
    :author: Frost Ming<mianghong@gmail.com>
"""
from __future__ import unicode_literals

import argparse
import json
import pkgutil
import random
import re

import colorama

from .consts import ALIGNMENT, BGCOLORS, CANDYCOLORS, CHARS, COLORS, FONTFACES, SIZE
from .colors import pen

colorama.init()


class Font:
    def __init__(self, name):
        self.name = name
        if name == FONTFACES.console:
            self.colors = 1
            self.lines = 1
            return
        font_face = json.loads(
            pkgutil.get_data(__package__, "fonts/{}.json".format(name)).decode("utf-8")
        )
        self.__dict__.update(font_face)

    def add_letter_spacing(self, output, letter_spacing):
        lines = len(output) - self.lines
        for i in range(lines, len(output)):
            idx = i - lines
            space = self.letterspace[idx] or " "
            output[i] += space * letter_spacing
        return output

    def add_char(self, output, char):
        lines = len(output) - self.lines
        for i in range(lines, len(output)):
            idx = i - lines
            output[i] += self.chars[char][idx]
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


def colorize(line, font_colors, colors):
    if font_colors > 1:
        for i in range(font_colors):
            try:
                color = colors[i]
            except IndexError:
                color = COLORS.system
            if color == COLORS.candy:
                color = random.choice(CANDYCOLORS.all())
            style = pen.style(color, False)
            line = re.sub("<c{}>".format(i + 1), style.open, line)
            line = re.sub("</c{}>".format(i + 1), style.close, line)
    elif font_colors == 1:
        try:
            color = colors[0]
        except IndexError:
            color = COLORS.system
        if color == COLORS.candy:
            color = random.choice(CANDYCOLORS.all())
        style = pen.style(color, False)
        line = style.open + re.sub(r"</?c\d+>", "", line) + style.close
    return line


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


def _find_left_most_non_space(line):
    return min(i for i, c in enumerate(line) if c.strip() != "")


def _find_right_most_non_space(line):
    return max(i for i, c in enumerate(line) if c.strip() != "")


def paint_gradient(
    output, gradient, independent_gradient, lines, font_lines, line_height, transition
):
    """Apply gradient colors to output"""
    if independent_gradient:
        buffer = []
        start = 0
        for _ in range(lines):
            temp = output[start : start + font_lines]
            add_line(
                buffer,
                paint_gradient(temp, gradient, False, 1, font_lines, 0, transition),
                line_height,
            )
            start += font_lines + line_height
        return buffer
    gradient = gradient or []
    output = [re.sub(r"</?c\d+>", "", line) for line in output]
    min_index = min(_find_left_most_non_space(line) for line in output if line.strip())
    max_index = max(_find_right_most_non_space(line) for line in output if line.strip())
    styles = pen.get_gradient(gradient, max_index - min_index + 1, transition)
    new_output = []
    for line in output:
        if not line.strip():
            new_output.append(line)
            continue
        temp = list(line)
        for i, style in zip(range(min_index, max_index + 1), styles):
            if i >= len(temp) or not temp[i].strip():
                continue
            temp[i] = style.open + temp[i] + style.close
        new_output.append("".join(temp))
    return new_output


def render(
    text,
    font=FONTFACES.block,
    size=SIZE,
    colors=None,
    background=BGCOLORS.transparent,
    align="left",
    letter_spacing=None,
    line_height=1,
    space=True,
    max_length=0,
    gradient=None,
    independent_gradient=False,
    transition=False,
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
    :param gradient: define the gradient color sequence
    :param independent_gradient: whether to apply gradient to each line independently
    :param transition: If set to True, will generate transition gradient colors
    :returns: the colored output string
    """
    font_face = get_font(font)
    colors = colors or []
    if colors and colors[0] != "system" and gradient:
        raise argparse.ArgumentError(
            "colors and gradient cannot be specified at the same time."
        )
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
        lines = 0
        if letter_spacing is None:
            letter_spacing = char_length(font_face.letterspace)
        line_length = char_length(font_face.buffer)
        max_chars = 0
        output = add_line([], font_face.buffer, line_height)
        lines += 1
        output = font_face.add_letter_spacing(output, letter_spacing)
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

            if max_chars > max_length != 0 or c == "|" or line_length > size[0]:
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
                output = font_face.add_letter_spacing(output, letter_spacing)

            if c != "|":
                output = font_face.add_char(output, c)
                output = font_face.add_letter_spacing(output, letter_spacing)

        output = align_text(output, line_length, font_face.lines, align, size)
        if gradient:
            output = paint_gradient(
                output,
                gradient,
                independent_gradient,
                lines,
                font_face.lines,
                line_height,
                transition,
            )

    output = [colorize(line, font_face.colors, colors) for line in output]
    if space:
        # Blank lines at the beginning and end
        output = [""] * 2 + output + [""] * 2
    if background != BGCOLORS.transparent:
        # Fill whitespaces to the full width.
        # See https://github.com/frostming/python-cfonts/issues/3
        output = [(line + " " * (size[0] - len(_strip_color(line)))) for line in output]
        style = pen.style(background, True)
        if output:
            output[0] = style.open + output[0]
            output[-1] += style.close
    return "\n".join(output)


def say(text, **options):
    """Render and write the output to stout.

    :param text: the string you want to render
    :param options: options passed as same as :func:`cfonts.render`
    :returns: None
    """
    write = render(text, **options)
    if write:
        print(write)


def _strip_color(text):
    regex = re.compile(r"\x1b\[\d+?m")
    return regex.sub("", text)

