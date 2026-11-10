"""Numeric CLI options must arrive as ints, not strings."""

import sys

import pytest

from cfonts.cli import parse_args


@pytest.fixture
def argv(monkeypatch):
    def _set(args):
        monkeypatch.setattr(sys, "argv", ["cfonts", *args])

    return _set


def test_line_height_is_coerced_to_int(argv):
    """-z 2 must give int 2, not str '2' (render does int arithmetic)."""
    argv(["-z", "2", "hi"])
    args = parse_args()
    assert args.line_height == 2
    assert isinstance(args.line_height, int)


def test_max_length_is_coerced_to_int(argv):
    """-m 10 must give int 10, not str '10' (render compares with >)."""
    argv(["-m", "10", "hi"])
    args = parse_args()
    assert args.max_length == 10
    assert isinstance(args.max_length, int)
