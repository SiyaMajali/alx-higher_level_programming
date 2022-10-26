#!/usr/bin/python3
'''
model read text file from UTF8 and prints it stdout
'''
def read_file(filename=""):
    '''
    reads text file(UTF8)  and print it stdout
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
