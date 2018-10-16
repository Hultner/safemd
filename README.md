![safemd](resources/castle_wide.jpg) 
[![Twitter Follow](https://img.shields.io/twitter/follow/ahultner.svg?style=social&label=Follow)](https://www.linkedin.com/in/hultner/)
[![Add Hultnér on LinkedIn](https://img.shields.io/badge/linkedin-hultner-blue.svg)](https://twitter.com/ahultner)
[![Build Status](https://travis-ci.org/Hultner/safemd.svg?branch=master)](https://travis-ci.org/Hultner/safemd)
![PyPI - Status](https://img.shields.io/pypi/status/safemd.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/21872a9d5f154750b457e6207a83298d)](https://www.codacy.com/app/Hultner/safemd?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Hultner/safemd&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/21872a9d5f154750b457e6207a83298d)](https://www.codacy.com/app/Hultner/safemd?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Hultner/safemd&amp;utm_campaign=Badge_Coverage)
![PyPI](https://img.shields.io/pypi/v/safemd.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/safemd.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![GitHub license](https://img.shields.io/github/license/Hultner/safemd.svg)](https://github.com/Hultner/safemd/blob/master/LICENSE)
# ♜ safemd
**A markdown renderer focusing on security first**  
Building upon the strong foundation of GitHub's fork of [cmark][] while adding
[additional security precautions](#precautions-taken) to be safe out of the box. 

When auditing applications rendering markdown from user input I noticed that
many popular markdown implementations are unsafe and vulnerable to XSS with
standard configuration. 

I am a strong believer in safe by default instead of opt-in security. Therefor 
I decided to build a library focusing on using the best tools for the job while
configuring them to safely render unsanitized user input. 

## Installation & usage
**Install through pip:**  
Any other tool using PyPI works fine as well, I always recommend using virtual
environments.
```shell
$ pip install safemd
```

Render standard markdown:
```python
import safemd

safemd.render(content)
```

Render GitHub Flavoured Markdown:
```python
import safemd

safemd.render(content, flavour="github")
```

## Precautions taken
The same [library][cmarkgfm] used for rendering markdown in the official PyPI 
Warehouse application is used by safemd. This is based on GitHub's 
battle-tested [fork][cmark] of CommonMark. We use this with the safety feature 
`CMARK_OPT_SAFE` enabled per default, so no one in your team accidentally let
insecure code slip through. As an additional safety layer safemd also pass the
output from cmark through a whitelist with [Bleach][bleach], Mozilla's HTML sanitizing
library. 

Automatic safety testing through Travis is also utilized, running daily even if
there are no new changes.

### Opt-out from safety features
There's a way to opt-out of these safety precautions for those cases where you 
have a genuine need, this way it's obvious for you and your team that these
places are to be considered with extra care.
```python
import safemd

# Disable additional whitelist sanitizing through bleach
safemd.render(content, UNSAFE_NO_BLEACH=True)

# Disable cmark safety functions
safemd.render(content, UNSAFE_CMARK_XSS=True)

```

## Is my application vulnerable? 
It's not uncommon for various markdown-renderers in production environments to
be open for XSS-exploits, some more widespread than others. A list of common
exploits have been assembled for your convenience, so you can test your current
and future code.
```md
[Just a link](javascript:alert("hi"))

[Normal link](data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGkiKTwvc2NyaXB0Pgo=) 

[Nothing fishy here](data:text/html;base64,PHNjcmlwdCBzcmM9Imh0dHBzOi8vZ2lzdGNkbi5naXRoYWNrLmNvbS9IdWx0bmVyL2JjMDIzOGJkOWIxZDI4M2JhMWM5NDczZjU0M2ZmZjc4L3Jhdy9kM2U5YWFkYTdlMGRlNzFkNmNlYTY1MDVmMTljZGE2NjE1MmE0MDFlL2hpLmpzIiBpbnRlZ3JpdHk9InNoYTM4NC0yaGZ6aFlkelB1SGd0S1E2Vk96UGlNbEN2Nzl3WDM1NzdxTDR3eWpmNWhMYkEvcW1BZHhCbXdxNGl6YXRwRy93IiBjcm9zc29yaWdpbj0iYW5vbnltb3VzIj48L3NjcmlwdD4=)
```

## Markdown XSS exploits found in the wild
Of course, this document wouldn't be complete without a list of markdown-based
XSS-exploits found in the wild. Most of these are from 2018 and 2017.
  - [Valve, store.steampowered.com markdown XSS](https://hackerone.com/reports/313250)
  - [GitLab, Markdown XSS](https://hackerone.com/reports/270999), [internal](https://about.gitlab.com/2017/10/17/gitlab-10-dot-0-dot-4-security-release/)
  - [PasteBin, markdown XSS (twice)](https://medium.com/@Nhoya/xss-in-pastebin-com-via-unsanitized-output-e216190b7949)
    - [CVE-2017-1000459](https://www.cvedetails.com/cve/CVE-2017-1000459/)
  - [Google Colaboratory, XSS + CSP Bypass](https://blog.bentkowski.info/2018/06/xss-in-google-colaboratory-csp-bypass.html)
  - [Zendesk, Markdown based Stored XSS](https://blog.0daylabs.com/2016/02/15/stored-xss-on-zendesk/)
  - [Streamlabs, account comromise XSS](https://blog.rockhouse.ga/2017/12/31/streamlabs-stored-xss-in-donation-page-leading-to-account-compromise-and-my-first-reward/)
  - [Commento](https://github.com/adtac/commento-ce/issues/154)
  - [Leanote](https://github.com/leanote/leanote/issues/719)
  - [Markdown's XSS Vulnerability (and how to mitigate it), showdownjs](https://github.com/showdownjs/showdown/wiki/Markdown%27s-XSS-Vulnerability-%28and-how-to-mitigate-it%29)
  - [And the list goes on…](https://www.google.com/search?q=markdown+xss)

## Found something
I am grateful for all suggestions, improvements and bugfixes. Feel free to send
a PR or create a GitHub Issue for anything that isn't sensitive and urgent.
Additional tests trying to break the security is especially appriciated.

I'm on [keybase](https://keybase.io/encrypt#hultner) for encrypted communication. 
Send an email to security on my own domain hultner.se. Be aware, I discard any
SPF, DMARC or DKIM-failing message, including SPF-Soft fail.

---
```
 .
..:
```

[cmark]: https://github.com/github/cmark-gfm
[cmarkgfm]: https://github.com/theacodes/cmarkgfm
[bleach]: https://github.com/mozilla/bleach
