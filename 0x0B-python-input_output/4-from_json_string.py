#!/usr/bin/python3
"""
create function from_json_string
"""


import json


def from_json_string(my_str):
    """
    fuction return object(python data structure) reprsented by JSON string
    """
    return json.loads(my_str)
