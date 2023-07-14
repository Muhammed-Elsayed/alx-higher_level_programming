#!/usr/bin/python3
"""documentaion"""


def read_file(filename=""):
    """reading an entire file and printing its content"""
    with open(filename, "r", encoding='utf-8') as myfile:
        content = myfile.read()
        print(content, end="")
