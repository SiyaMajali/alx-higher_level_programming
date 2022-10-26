#!/usr/bin/python3
"""
contains function save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    '''
    function that writes an object to a text file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
