"""
Markdown input examples for testing

Author: Alexander Hultnér
"""


unsafe_xss = """
[Just a link](javascript:alert("hi"))

[Normal link](data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGkiKTwvc2NyaXB0Pgo=)

[Nothing fishy here](data:text/html;base64,PHNjcmlwdCBzcmM9Imh0dHBzOi8vZ2lzdGNkbi5naXRoYWNrLmNvbS9IdWx0bmVyL2JjMDIzOGJkOWIxZDI4M2JhMWM5NDczZjU0M2ZmZjc4L3Jhdy9kM2U5YWFkYTdlMGRlNzFkNmNlYTY1MDVmMTljZGE2NjE1MmE0MDFlL2hpLmpzIiBpbnRlZ3JpdHk9InNoYTM4NC0yaGZ6aFlkelB1SGd0S1E2Vk96UGlNbEN2Nzl3WDM1NzdxTDR3eWpmNWhMYkEvcW1BZHhCbXdxNGl6YXRwRy93IiBjcm9zc29yaWdpbj0iYW5vbnltb3VzIj48L3NjcmlwdD4=)
"""
