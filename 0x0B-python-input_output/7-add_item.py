#!/usr/bin/python3
"""script that adds all arguments to a Python list, and save them to a file"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

try:
    existing_list = load_from_json_file(filename)

except FileNotFoundError:
    existing_list = []

new_list = existing_list + args

save_to_json_file(new_list, filename)
