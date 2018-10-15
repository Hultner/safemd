"""Testing safemd

Trying to focus on security in these tests, upstream libraries are responsible
for otherwise correct markdown rendering.

Author: Alexander Hultnér, 2018
"""

from .payloads import unsafe_xss, default, NO_BLEACH, CMARK_XSS, CMARK_XSS_NO_BLEACH
from safemd import render


def test_nothing():
    assert render(None) == None


def test_md_xss_default():
    assert render(unsafe_xss) == default
    assert render(unsafe_xss, flavour="github") == default


def test_md_xss_no_bleach():
    assert render(unsafe_xss, UNSAFE_NO_BLEACH=True) == NO_BLEACH


def test_md_xss_cmark_xss():
    assert render(unsafe_xss, UNSAFE_CMARK_XSS=True) == CMARK_XSS


def test_md_xss_cmark_xss_no_bleach():
    assert (
        render(unsafe_xss, UNSAFE_CMARK_XSS=True, UNSAFE_NO_BLEACH=True)
        == CMARK_XSS_NO_BLEACH
    )
