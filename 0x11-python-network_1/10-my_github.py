#!/usr/bin/python3
"""Take GitHub credentials"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    session = requests.Session()
    response = session.get(url, auth=(sys.argv[1], sys.argv[2]))
    r = response.json()
    print(r.get('id'))
