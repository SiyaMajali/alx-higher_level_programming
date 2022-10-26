#!/usr/bin/python3
"""
contans append_write function
"""


def append_write(filename="", text=""):
    """
    append string end of text file(UTF8) & returns number of char added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
