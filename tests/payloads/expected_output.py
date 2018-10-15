"""
Expected outputs from safemd

Author: Alexander Hultnér
"""

default = '<p><a href="" rel="nofollow">Just a link</a></p>\n<p><a href="" rel="nofollow">Normal link</a></p>\n<p><a href="" rel="nofollow">Nothing fishy here</a></p>\n'

NO_BLEACH = '<p><a href="">Just a link</a></p>\n<p><a href="">Normal link</a></p>\n<p><a href="">Nothing fishy here</a></p>\n'

CMARK_XSS = "<p><a>Just a link</a></p>\n<p><a>Normal link</a></p>\n<p><a>Nothing fishy here</a></p>\n"

CMARK_XSS_NO_BLEACH = '<p><a href="javascript:alert(%22hi%22)">Just a link</a></p>\n<p><a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGkiKTwvc2NyaXB0Pgo=">Normal link</a></p>\n<p><a href="data:text/html;base64,PHNjcmlwdCBzcmM9Imh0dHBzOi8vZ2lzdGNkbi5naXRoYWNrLmNvbS9IdWx0bmVyL2JjMDIzOGJkOWIxZDI4M2JhMWM5NDczZjU0M2ZmZjc4L3Jhdy9kM2U5YWFkYTdlMGRlNzFkNmNlYTY1MDVmMTljZGE2NjE1MmE0MDFlL2hpLmpzIiBpbnRlZ3JpdHk9InNoYTM4NC0yaGZ6aFlkelB1SGd0S1E2Vk96UGlNbEN2Nzl3WDM1NzdxTDR3eWpmNWhMYkEvcW1BZHhCbXdxNGl6YXRwRy93IiBjcm9zc29yaWdpbj0iYW5vbnltb3VzIj48L3NjcmlwdD4=">Nothing fishy here</a></p>\n'
