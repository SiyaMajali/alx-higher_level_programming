#!/usr/bin/python3
"""
contains to_json_string function
"""


import json


def to_json_string(my_obj):
    """
    function return the json repersention of an objecrt(string)
    """
    return json.dumps(my_obj)
