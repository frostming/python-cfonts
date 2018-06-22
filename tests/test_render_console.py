from cfonts.core import render_console


def test_render_console_default():
    assert render_console("text", size=(100, 10)) == ["text"]
    assert render_console("text|text", size=(100, 10)) == ["text", "text"]


def test_render_console_long_text():
    assert (
        render_console("this is a very long line to test multi lines", size=(10, 10))
        == ["this is a", "very long", "line to te", "st multi l", "ines"]
    )


def test_render_console_align():
    assert render_console("center", align="center", size=(10, 10)) == ["  center"]

    assert render_console("right", align="right", size=(10, 10)) == ["     right"]


def test_render_console_letter_spacing():
    assert render_console("text", letter_spacing=2, size=(10, 10)) == ["t e x t"]
    assert render_console("text", letter_spacing=3, size=(100, 10)) == ["t  e  x  t"]
    assert (
        render_console("text", letter_spacing=10, size=(100, 10))
        == ["t         e         x         t"]
    )

    assert (
        render_console("text|text", letter_spacing=2, size=(10, 10))
        == ["t e x t", "t e x t"]
    )
    assert (
        render_console("text|text", letter_spacing=3, size=(100, 10))
        == ["t  e  x  t", "t  e  x  t"]
    )
    assert (
        render_console("text|text", letter_spacing=10, size=(100, 10))
        == ["t         e         x         t", "t         e         x         t"]
    )


def test_render_console_line_height():
    assert render_console("text", line_height=2, size=(100, 10)) == ["text", ""]
    assert render_console("text", line_height=3, size=(100, 10)) == ["text", "", ""]
    assert render_console("text", line_height=10, size=(100, 10)) == ["text"] + [""] * 9

    assert (
        render_console("text|text|text", line_height=2, size=(100, 10))
        == ["text", ""] * 3
    )
    assert (
        render_console("text|text|text", line_height=3, size=(100, 10))
        == ["text", "", ""] * 3
    )
    assert (
        render_console("text|text|text", line_height=10, size=(100, 10))
        == (["text"] + [""] * 9) * 3
    )


def test_render_console_line_break():
    assert (
        render_console("this is a long line", line_height=2, size=(10, 10))
        == ["this is a", "", "long line", ""]
    )
    assert (
        render_console("this is a long line", line_height=3, size=(10, 10))
        == ["this is a", "", "", "long line", "", ""]
    )
    assert (
        render_console("this is a long line", line_height=10, size=(10, 10))
        == [
            "this is a",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "long line",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
    )


def test_render_console_color(strip_color):
    assert render_console("text", colors=["red"], size=(100, 10)) == ["text"]
    output = render_console("text", colors=["candy"], size=(100, 10))
    assert strip_color(output[0]) == "text"
    assert len(output[0]) > len("text")
