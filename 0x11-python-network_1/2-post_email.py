#!/usr/bin/python3
"""Script that sends a POST request"""
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode()
    req = urllib.request.Request(sys.argv[1], data=data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()
    print(resp.decode('utf8'))
