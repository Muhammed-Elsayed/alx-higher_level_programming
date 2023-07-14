#!/usr/bin/python3
"""documentaion"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of chars"""
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.write(text)
        return (len(text))
