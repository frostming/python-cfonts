"""add_char and add letter space function"""


def test_add_single_line(font):
    fontface = font({"A": ["A"]})
    assert fontface.add_char([""], "A", []) == ["A"]
    assert fontface.add_char([""], "A", ["red"]) == ["\x1b[31mA\x1b[39m"]


def test_add_multi_lines(font):
    fontface = font({"A": [",-,", "|-|", "| |"]})
    assert fontface.add_char(["", "", ""], "A", []) == fontface.chars["A"]
    expected = ["\x1b[31m,-,\x1b[39m", "\x1b[31m|-|\x1b[39m", "\x1b[31m| |\x1b[39m"]
    assert fontface.add_char(["", "", ""], "A", ["red"]) == expected


def test_add_multi_lines_with_color(font):
    fontface = font({"A": [",<c1>-</c1>,", "|-|", "| <c2>|</c2>"]}, 2)
    expected = [",\x1b[31m-\x1b[39m,", "|-|", "| \x1b[31m|\x1b[39m"]
    assert fontface.add_char(["", "", ""], "A", ["red", "red"]) == expected


def test_add_letter_spacing_single_line_no_color(font):
    assert font(letterspace=[" "]).add_letter_spacing(["", "", ""], [], 1) == [
        "",
        "",
        " ",
    ]
    assert font(letterspace=[""]).add_letter_spacing(["", "", ""], [], 1) == [
        "",
        "",
        " ",
    ]
    assert font(letterspace=[""]).add_letter_spacing(["", "", ""], [], 2) == [
        "",
        "",
        "  ",
    ]


def test_add_letter_spacing_single_line_color(font):
    assert font(letterspace=[" "]).add_letter_spacing(["", "", ""], ["red"], 1) == [
        "",
        "",
        "\x1b[31m \x1b[39m",
    ]
    assert font(colors=2, letterspace=["<c1> </c1>"]).add_letter_spacing(
        ["", "", ""], ["red", "red"], 1
    ) == ["", "", "\x1b[31m \x1b[39m"]
    assert font(colors=2, letterspace=["<c2>#</c2>"]).add_letter_spacing(
        ["", "", ""], ["red", "red"], 1
    ) == ["", "", "\x1b[31m#\x1b[39m"]


def test_add_letter_spacing_multi_lines(font):
    assert font(letterspace=[" ", " ", " "]).add_letter_spacing([""] * 6, [], 1) == [
        "",
        "",
        "",
        " ",
        " ",
        " ",
    ]
    assert font(letterspace=["_", "_", "_"]).add_letter_spacing([""] * 6, [], 1) == [
        "",
        "",
        "",
        "_",
        "_",
        "_",
    ]


def test_add_letter_spacing_multi_line_one_color(font):
    assert (
        font(letterspace=[" ", " ", " "]).add_letter_spacing([""] * 6, ["red"], 1)
        == [""] * 3 + ["\x1b[31m \x1b[39m"] * 3
    )
    assert (
        font(letterspace=["_", "_", "_"]).add_letter_spacing([""] * 6, ["red"], 1)
        == [""] * 3 + ["\x1b[31m_\x1b[39m"] * 3
    )


def test_add_letter_spacing_multi_line_multi_colors(font):
    assert (
        font(colors=2, letterspace=["<c1> </c1>"] * 3).add_letter_spacing(
            [""] * 6, ["red", "red"], 1
        )
        == [""] * 3 + ["\x1b[31m \x1b[39m"] * 3
    )
    assert (
        font(colors=2, letterspace=["<c2> </c2>"] * 3).add_letter_spacing(
            [""] * 6, ["red", "red"], 1
        )
        == [""] * 3 + ["\x1b[31m \x1b[39m"] * 3
    )
    assert (
        font(colors=2, letterspace=["<c1>_</c1>"] * 3).add_letter_spacing(
            [""] * 6, ["red", "red"], 1
        )
        == [""] * 3 + ["\x1b[31m_\x1b[39m"] * 3
    )
    assert (
        font(colors=2, letterspace=["<c2>_</c2>"] * 3).add_letter_spacing(
            [""] * 6, ["red", "red"], 1
        )
        == [""] * 3 + ["\x1b[31m_\x1b[39m"] * 3
    )
