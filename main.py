from __future__ import annotations
def run(text,width=80):
 import textwrap
 return "\n".join(textwrap.wrap(text,width=width))
