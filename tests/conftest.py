"""pytest configuration"""
import re
import pytest
from cfonts.core import Font


@pytest.fixture
def font():
    def font_factory(chars={}, colors=1, letterspace=[], buffer=[]):
        rv = Font("console")
        rv.chars = chars
        if chars:
            rv.lines = len(chars[list(chars.keys())[0]])
        else:
            rv.lines = len(letterspace)
        rv.colors = colors
        rv.letterspace = letterspace
        rv.buffer = buffer
        return rv

    return font_factory


@pytest.fixture
def strip_color():
    def func(text):
        REGEX = re.compile(r'\x1b\[\d+?m')
        return REGEX.sub('', text)
    return func
