#!/usr/bin/python3
"""Display the value in the X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    session = requests.Session()
    response = session.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
