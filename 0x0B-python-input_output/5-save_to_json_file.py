#!/usr/bin/python3
"""convert to json and write to file"""
import json


def save_to_json_file(my_obj, filename):
    """convert to json and write to file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
