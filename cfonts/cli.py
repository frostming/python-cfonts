"""
    Python cFonts
    =============
    Sexy fonts for the console.

    :license: GNU GPLv2
    :author: Frost Ming<mianghong@gmail.com>
"""
import click
from .consts import *  # noqa
from .core import say, render


@click.option(
    "-f",
    "--font",
    default=FONTFACES.block,
    type=click.Choice(FONTFACES.all()),
    help="Use to define the font face",
)
@click.option(
    "-c", "--colors", default=COLORS.system, help="Use to define the font color"
)
@click.option(
    "-b",
    "--background",
    default=BGCOLORS.transparent,
    type=click.Choice(BGCOLORS.all()),
    help="Use to define the background color",
)
@click.option(
    "-a",
    "--align",
    default="left",
    type=click.Choice(ALIGNMENT),
    help="Use to align your text output",
)
@click.option(
    "-l", "--letter-spacing", type=int, help="Use to define your letter spacing"
)
@click.option("-z", "--line-height", default=1, help="Use to define your line height")
@click.option(
    "-s",
    "--spaceless",
    default=True,
    is_flag=True,
    help="Use to disable the padding around your output",
)
@click.option(
    "-m",
    "--max-length",
    default=0,
    help="Use to define the amount of maximum characters per line",
)
@click.argument("text", required=True)
@click.version_option(
    prog_name=render("cfonts", font="console", colors=["candy"], space=False)
)
@click.command(
    help="This is a tool for sexy fonts in the console. Give your cli some love."
)
def cli(
    text,
    font,
    colors,
    background,
    align,
    letter_spacing,
    line_height,
    spaceless,
    max_length,
):
    colors = colors.split(",")
    options = {
        "font": font,
        "colors": colors,
        "background": background,
        "align": align,
        "line_height": line_height,
        "space": spaceless,
        "max_length": max_length,
    }
    if letter_spacing is not None:
        options["letter_spacing"] = letter_spacing
    say(text, **options)
