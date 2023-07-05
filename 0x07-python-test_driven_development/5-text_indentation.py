#!/usr/bin/python3
"""comment"""


def print_with_newlines(text):
    '''printing two lines'''
    for char in ['.', '?', ':']:
        text = text.replace(char, char + '\n\n')
    print(text)
