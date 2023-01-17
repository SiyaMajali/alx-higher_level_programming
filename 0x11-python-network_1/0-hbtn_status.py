#!/usr/bin/python3
import urllib.request as request

def fetcher():
    """fetcher"""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as request:
        html = request.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))

if __name__ == "__main__":
    fetcher()
