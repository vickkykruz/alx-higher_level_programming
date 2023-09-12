#!/usr/bin/python3
"""
    This is a script that add all arguments to a Python list, and then save
    then save them to a file:
        => Using the function save_to_json_file from 5-save_to_json_file
        => Using the function load_from_json_file from 6-load_from_json_file
"""


import json

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    obj_json = load_from_json_file(filename)
except FileNotFoundError:
    obj_json = []
except json.decode.JSONDecodeError:
    obj_json = []

for ele in sys.argv[1:]:
    obj_json += [ele]
    save_to_json_file(obj_json, filename)
