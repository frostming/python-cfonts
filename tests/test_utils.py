# -*- coding: utf-8 -*-
"""Test utility functions"""
import pytest

from cfonts.core import add_line, char_length, align_text, clean_input, colorize
from cfonts.colors import (
    get_closest,
    hex_to_rgb,
    AnsiPen,
    TrueColorPen,
    rgb_to_hex,
    rgb_to_hsv,
    hsv_to_rgb,
)


def test_add_line_single_font():
    text = ["line1", "line2"]

    assert add_line(text[:], [""], 0) == text + [""]
    assert add_line(text[:], [""], 1) == text + [""] * 2
    assert add_line(text[:], [""], 5) == text + [""] * 6


def test_add_line_multi_font():
    text = [",-, ,-,", "|-| |-}", "| | |_}"]

    assert add_line(text[:], [""] * 3, 0) == text + [""] * 3
    assert add_line(text[:], [""] * 3, 1) == text + [""] * 4
    assert add_line(text[:], [""] * 3, 10) == text + [""] * 13


def test_char_length():
    text_1 = [""]
    text_2 = ["", "  "]
    text_3 = ["      ", ""]
    text_4 = ["", "   ", ""]
    text_5 = [" ", "", "        ", "", "            ", " "]

    assert (char_length(text_1, 0)) == 0
    assert (char_length(text_2, 0)) == 2
    assert (char_length(text_3, 0)) == 6
    assert (char_length(text_4, 0)) == 3
    assert (char_length(text_5, 0)) == 12

    assert (char_length(text_1, 5)) == 1
    assert (char_length(text_2, 5)) == 2
    assert (char_length(text_3, 5)) == 6
    assert (char_length(text_4, 5)) == 3
    assert (char_length(text_5, 5)) == 12

    assert (char_length(text_1, 1)) == 1


def test_align_center():
    assert align_text(["x"], 1, 1, "center", (21, 2)) == ["          x"]
    assert align_text(["x"], 1, 1, "center", (1, 2)) == ["x"]


def test_align_right():
    assert align_text(["x"], 1, 1, "right", (11, 2)) == ["          x"]
    assert align_text(["x"], 1, 1, "right", (1, 2)) == ["x"]


def test_align_left():
    assert align_text(["x"], 1, 1, "left", (11, 2)) == ["x"]


def test_clean_input():
    from cfonts.consts import CHARS

    assert clean_input("abcd", "ABC") == "abc"
    assert clean_input("abdc", "ABC") == "abc"
    assert clean_input("ab c", "ABC") == "abc"
    assert clean_input("abc", "ABC") == "abc"
    assert clean_input("abc•", "ABC") == "abc"
    assert clean_input(" abc", "ABC") == "abc"
    assert clean_input(CHARS) == CHARS


def test_colorize_without_color_placeholder():
    text = "test string without color placeholders"
    assert colorize(text, 1, []) == text
    assert colorize(text, 1, ["red"]) == "\x1b[31m{}\x1b[39m".format(text)


def test_colorize_with_two_colors():
    text = "test string <c1>with</c1> one <c2>color</c2> placeholders"
    assert (
        colorize(text, 2, ["red", "red"])
        == "test string \x1b[31mwith\x1b[39m one \x1b[31mcolor\x1b[39m placeholders"
    )


def test_colorize_candy_color(strip_color):
    text = colorize("<c1>text</c1>", 1, ["candy"])
    assert strip_color(text) == "text"
    assert len(text) > len("text")


@pytest.mark.parametrize(
    "hex_string,rgb", [("#111", (17, 17, 17)), ("#51c7bd", (81, 199, 189))]
)
def test_hex_to_rgb(hex_string, rgb):
    assert hex_to_rgb(hex_string) == rgb


@pytest.mark.parametrize(
    "hex_string,target", [("#111", "black"), ("#ff5f52", "bright_red")]
)
def test_get_closest_color(hex_string, target):
    assert get_closest(hex_to_rgb(hex_string)) == target


@pytest.mark.parametrize(
    "color,is_background,style",
    [
        ("red", False, ("\x1b[31m", "\x1b[39m")),
        ("red", True, ("\x1b[41m", "\x1b[49m")),
        ("system", False, ("", "")),
    ],
)
def test_ansi_pen(color, is_background, style):
    pen = AnsiPen()
    assert pen.style(color, is_background) == style


@pytest.mark.parametrize(
    "color,is_background,style",
    [
        ("#ff5f52", False, ("\x01\x1b[38;2;255;95;82m", "\x1b[39m")),
        ("#ff5f52", True, ("\x01\x1b[48;2;255;95;82m", "\x1b[49m")),
    ],
)
def test_truecolor_pen(color, is_background, style):
    pen = TrueColorPen()
    assert pen.style(color, is_background) == style


def test_color_conversion():
    hex_string = "#51c7bd"
    rgb = (81, 199, 189)
    hsv = rgb_to_hsv(rgb)
    assert hex_to_rgb(hex_string) == rgb
    assert rgb_to_hex(rgb) == hex_string

    assert rgb_to_hsv(rgb) == hsv
    assert hsv_to_rgb(hsv) == rgb


def test_generate_gradients():
    pen = AnsiPen()
    assert len(pen.get_gradient(["red", "green"], 20)) == 20
    assert len(pen.get_gradient(["red", "green"], 23)) == 23

    assert len(pen.get_gradient(["red", "yellow", "green"], 20, True)) == 20
    assert len(pen.get_gradient(["red", "yellow", "green"], 23, True)) == 23
