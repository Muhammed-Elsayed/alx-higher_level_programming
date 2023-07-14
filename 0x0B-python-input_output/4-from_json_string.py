#!/usr/bin/python3
"""converting from json form"""
import json


def from_json_string(my_obj):
    """convert the object from json"""
    return json.loads(my_obj)
