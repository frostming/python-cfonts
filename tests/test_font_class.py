"""add_char and add letter space function"""


def test_add_single_line(font):
    fontface = font({"A": ["A"]})
    assert fontface.add_char([""], "A") == ["A"]


def test_add_multi_lines(font):
    fontface = font({"A": [",-,", "|-|", "| |"]})
    assert fontface.add_char(["", "", ""], "A") == fontface.chars["A"]


def test_add_letter_spacing_single_line_no_color(font):
    assert font(letterspace=[" "]).add_letter_spacing(["", "", ""], 1) == [
        "",
        "",
        " ",
    ]
    assert font(letterspace=[""]).add_letter_spacing(["", "", ""], 1) == [
        "",
        "",
        " ",
    ]
    assert font(letterspace=[""]).add_letter_spacing(["", "", ""], 2) == [
        "",
        "",
        "  ",
    ]


def test_add_letter_spacing_multi_lines(font):
    assert font(letterspace=[" ", " ", " "]).add_letter_spacing([""] * 6, 1) == [
        "",
        "",
        "",
        " ",
        " ",
        " ",
    ]
    assert font(letterspace=["_", "_", "_"]).add_letter_spacing([""] * 6, 1) == [
        "",
        "",
        "",
        "_",
        "_",
        "_",
    ]

