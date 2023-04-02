#!/usr/bin/python3
"""Print status code"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
        print(html.decode('utf8'))
    except urllib.error.HTTPError as status:
        print('Error code: {}'.format(status.code))
