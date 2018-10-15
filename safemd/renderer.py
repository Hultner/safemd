"""
safemd – Safety first markdown rendering

Author: Alexander Hultnér, 2018

"""

from typing import Optional
from cmarkgfm.cmark import markdown_to_html, github_flavored_markdown_to_html, Options
from .clean import clean


def render(
    content: str,
    flavour: str = "",
    *,
    UNSAFE_NO_BLEACH: bool = False,
    UNSAFE_CMARK_XSS: bool = False,
) -> Optional[str]:

    if not content:
        # No content, nothing to do here
        return None

    if flavour.lower() in ["gfm", "github"]:
        md_render = github_flavored_markdown_to_html
    else:
        md_render = markdown_to_html

    if UNSAFE_CMARK_XSS:
        # Use unsafe rendering in cmark
        options = 0
    else:
        options = Options.CMARK_OPT_SAFE

    output = md_render(content, options=options)

    if UNSAFE_NO_BLEACH or output is None:
        # No bleach or no output from renderer
        return output

    return clean(output)
