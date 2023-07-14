#!/usr/bin/python3
"""documentaion"""


import os


def read_file(filename=""):
    with open(filename, "r", encoding='utf-8') as myfile:
        content = myfile.read()
        print(content)
