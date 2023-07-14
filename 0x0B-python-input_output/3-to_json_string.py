#!/usr/bin/python3
"""converting to json form"""
import json


def to_json_string(my_obj):
    """convert the object to json"""
    return json.dump(my_obj)
