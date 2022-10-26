#!/usr/bin/python3
"""
have function load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
    function that creates an object from json file
    """
    with open(filename, 'r', encoding='utf8') as f:
        return json.load(f)
