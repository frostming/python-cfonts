"""Test utility functions"""
from cfonts.core import add_line, char_length, align_text, clean_input, colorize


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
    assert colorize(text, 1, ["red"]) == f"\x1b[31m{text}\x1b[39m"


def test_colorize_with_two_colors():
    text = "test string <c1>with</c1> one <c2>color</c2> placeholders"
    assert (
        colorize(text, 2, ["red", "red"])
        == "test string \x1b[31mwith\x1b[39m one \x1b[31mcolor\x1b[39m placeholders"
    )
