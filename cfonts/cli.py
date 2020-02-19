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


class CFontCommand(click.Command):
    def format_help(self, ctx, formatter):
        self.format_help_text(ctx, formatter)
        self.format_usage(ctx, formatter)
        self.format_options(ctx, formatter)
        self.format_epilog(ctx, formatter)

    def format_help_text(self, ctx, formatter):
        banner = render("cfonts", gradient=["bright_red", "bright_green"])
        formatter.write(banner)
        formatter.write_text(self.help)
        formatter.write_paragraph()


@click.command(cls=CFontCommand)
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
@click.option(
    "-g", "--gradient", help="Define gradient colors(separated by comma)",
)
@click.option(
    "-i",
    "--independent-gradient",
    is_flag=True,
    help="Set this option to re-calculate the gradient colors for each new line."
    "Only works in combination with the gradient option.",
)
@click.option(
    "-t",
    "--transition-gradient",
    "transition",
    is_flag=True,
    help="Set this option to generate your own gradients. "
    "Each color set in the gradient option will then be transitioned to directly.",
)
@click.version_option(
    None,
    "-V",
    "--version",
    prog_name=render("cfonts", font="console", colors=["candy"], space=False),
)
@click.argument("text", required=True)
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
    gradient,
    independent_gradient,
    transition,
):
    """This is a tool for sexy fonts in the console. Give your cli some love."""
    colors = [c.strip() for c in colors.split(",")]
    if gradient:
        gradient = [g.strip() for g in gradient.split(",")]
    options = {
        "font": font,
        "colors": colors,
        "background": background,
        "align": align,
        "line_height": line_height,
        "space": spaceless,
        "max_length": max_length,
        "gradient": gradient,
        "independent_gradient": independent_gradient,
        "transition": transition,
    }
    if letter_spacing is not None:
        options["letter_spacing"] = letter_spacing
    say(text, **options)
