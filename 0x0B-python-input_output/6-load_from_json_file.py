#!/usr/bin/python3
"""module"""
import json


def load_from_json_file(filename):
    """loads from json file"""
    with open(filename) as myfile:
        return (json.load(myfile))
