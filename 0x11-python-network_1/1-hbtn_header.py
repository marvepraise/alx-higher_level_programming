#!/usr/bin/python3
"""Script fetching the value of X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.getheader('X-Request-Id')
    print(header)
