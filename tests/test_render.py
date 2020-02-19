# -*- coding: utf-8 -*-
# flake8: noqa
from __future__ import unicode_literals
import pytest
from cfonts import render


def test_render_console():
    text = render("text", font="console", size=(100, 10))
    assert text == "\n\ntext\n\n"


def test_render_console_with_color():
    text = render("text", font="console", colors=["red"], size=(100, 10))
    assert text == "\n\n\x1b[31mtext\x1b[39m\n\n"


def test_render_invalid_input():
    with pytest.raises(Exception):
        render(None)
    with pytest.raises(Exception):
        render("text", font="notfound")
    with pytest.raises(Exception):
        render("text", align="notfound")
    with pytest.raises(Exception):
        render("text", colors=["notfound"])
    with pytest.raises(Exception):
        render("text", background="notfound")


def test_render_block_font():
    text = render("text", size=(100, 10))
    assert text == (
        "\n\n"
        " ████████╗ ███████╗ ██╗  ██╗ ████████╗ \n"
        " ╚══██╔══╝ ██╔════╝ ╚██╗██╔╝ ╚══██╔══╝ \n"
        "    ██║    █████╗    ╚███╔╝     ██║    \n"
        "    ██║    ██╔══╝    ██╔██╗     ██║    \n"
        "    ██║    ███████╗ ██╔╝ ██╗    ██║    \n"
        "    ╚═╝    ╚══════╝ ╚═╝  ╚═╝    ╚═╝    \n\n"
    )


def test_render_letter_spacing():
    text = render("text", letter_spacing=2, size=(100, 10))
    assert text == (
        "\n\n"
        "  ████████╗  ███████╗  ██╗  ██╗  ████████╗  \n"
        "  ╚══██╔══╝  ██╔════╝  ╚██╗██╔╝  ╚══██╔══╝  \n"
        "     ██║     █████╗     ╚███╔╝      ██║     \n"
        "     ██║     ██╔══╝     ██╔██╗      ██║     \n"
        "     ██║     ███████╗  ██╔╝ ██╗     ██║     \n"
        "     ╚═╝     ╚══════╝  ╚═╝  ╚═╝     ╚═╝     \n\n"
    )
    text = render("text", letter_spacing=10, size=(100, 10))
    assert text == (
        "\n\n"
        "          ████████╗          ███████╗          ██╗  ██╗          ████████╗          \n"
        "          ╚══██╔══╝          ██╔════╝          ╚██╗██╔╝          ╚══██╔══╝          \n"
        "             ██║             █████╗             ╚███╔╝              ██║             \n"
        "             ██║             ██╔══╝             ██╔██╗              ██║             \n"
        "             ██║             ███████╗          ██╔╝ ██╗             ██║             \n"
        "             ╚═╝             ╚══════╝          ╚═╝  ╚═╝             ╚═╝             \n\n"
    )


def test_render_center_block_font():
    assert render("text", align="center", size=(50, 10)) == (
        "\n\n"
        "      ████████╗ ███████╗ ██╗  ██╗ ████████╗ \n"
        "      ╚══██╔══╝ ██╔════╝ ╚██╗██╔╝ ╚══██╔══╝ \n"
        "         ██║    █████╗    ╚███╔╝     ██║    \n"
        "         ██║    ██╔══╝    ██╔██╗     ██║    \n"
        "         ██║    ███████╗ ██╔╝ ██╗    ██║    \n"
        "         ╚═╝    ╚══════╝ ╚═╝  ╚═╝    ╚═╝    \n\n"
    )


def test_render_right_block_font():
    assert render("text", align="right", size=(50, 10)) == (
        "\n\n"
        "            ████████╗ ███████╗ ██╗  ██╗ ████████╗ \n"
        "            ╚══██╔══╝ ██╔════╝ ╚██╗██╔╝ ╚══██╔══╝ \n"
        "               ██║    █████╗    ╚███╔╝     ██║    \n"
        "               ██║    ██╔══╝    ██╔██╗     ██║    \n"
        "               ██║    ███████╗ ██╔╝ ██╗    ██║    \n"
        "               ╚═╝    ╚══════╝ ╚═╝  ╚═╝    ╚═╝    \n\n"
    )


def test_render_break_new_line():
    assert render("text", size=(20, 10)) == (
        "\n\n"
        " ████████╗ ███████╗ \n"
        " ╚══██╔══╝ ██╔════╝ \n"
        "    ██║    █████╗   \n"
        "    ██║    ██╔══╝   \n"
        "    ██║    ███████╗ \n"
        "    ╚═╝    ╚══════╝ \n\n"
        " ██╗  ██╗ ████████╗ \n"
        " ╚██╗██╔╝ ╚══██╔══╝ \n"
        "  ╚███╔╝     ██║    \n"
        "  ██╔██╗     ██║    \n"
        " ██╔╝ ██╗    ██║    \n"
        " ╚═╝  ╚═╝    ╚═╝    \n\n"
    )


def test_render_add_line_break():
    assert render("te|xt", size=(100, 10)) == (
        "\n\n"
        " ████████╗ ███████╗ \n"
        " ╚══██╔══╝ ██╔════╝ \n"
        "    ██║    █████╗   \n"
        "    ██║    ██╔══╝   \n"
        "    ██║    ███████╗ \n"
        "    ╚═╝    ╚══════╝ \n\n"
        " ██╗  ██╗ ████████╗ \n"
        " ╚██╗██╔╝ ╚══██╔══╝ \n"
        "  ╚███╔╝     ██║    \n"
        "  ██╔██╗     ██║    \n"
        " ██╔╝ ██╗    ██║    \n"
        " ╚═╝  ╚═╝    ╚═╝    \n\n"
    )


def test_render_add_line_height():
    assert render("te|xt", line_height=2, size=(100, 10)) == (
        "\n\n"
        " ████████╗ ███████╗ \n"
        " ╚══██╔══╝ ██╔════╝ \n"
        "    ██║    █████╗   \n"
        "    ██║    ██╔══╝   \n"
        "    ██║    ███████╗ \n"
        "    ╚═╝    ╚══════╝ \n\n\n"
        " ██╗  ██╗ ████████╗ \n"
        " ╚██╗██╔╝ ╚══██╔══╝ \n"
        "  ╚███╔╝     ██║    \n"
        "  ██╔██╗     ██║    \n"
        " ██╔╝ ██╗    ██║    \n"
        " ╚═╝  ╚═╝    ╚═╝    \n\n"
    )


def test_render_ignore_non_supported():
    assert render("te*xt", size=(100, 10)) == (
        "\n\n"
        " ████████╗ ███████╗ ██╗  ██╗ ████████╗ \n"
        " ╚══██╔══╝ ██╔════╝ ╚██╗██╔╝ ╚══██╔══╝ \n"
        "    ██║    █████╗    ╚███╔╝     ██║    \n"
        "    ██║    ██╔══╝    ██╔██╗     ██║    \n"
        "    ██║    ███████╗ ██╔╝ ██╗    ██║    \n"
        "    ╚═╝    ╚══════╝ ╚═╝  ╚═╝    ╚═╝    \n\n"
    )


def test_render_remove_space():
    assert render("text", space=False, size=(100, 10)) == (
        " ████████╗ ███████╗ ██╗  ██╗ ████████╗ \n"
        " ╚══██╔══╝ ██╔════╝ ╚██╗██╔╝ ╚══██╔══╝ \n"
        "    ██║    █████╗    ╚███╔╝     ██║    \n"
        "    ██║    ██╔══╝    ██╔██╗     ██║    \n"
        "    ██║    ███████╗ ██╔╝ ██╗    ██║    \n"
        "    ╚═╝    ╚══════╝ ╚═╝  ╚═╝    ╚═╝    "
    )


def test_render_background():
    assert render("text", background="red", size=(50, 10)) == (
        "\x1b[41m{0}\n{0}\n"
        " ████████╗ ███████╗ ██╗  ██╗ ████████╗ {1}\n"
        " ╚══██╔══╝ ██╔════╝ ╚██╗██╔╝ ╚══██╔══╝ {1}\n"
        "    ██║    █████╗    ╚███╔╝     ██║    {1}\n"
        "    ██║    ██╔══╝    ██╔██╗     ██║    {1}\n"
        "    ██║    ███████╗ ██╔╝ ██╗    ██║    {1}\n"
        "    ╚═╝    ╚══════╝ ╚═╝  ╚═╝    ╚═╝    {1}\n{0}\n{0}\x1b[49m"
    ).format(" " * 50, " " * 11)
