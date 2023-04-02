#!/usr/bin/python3
"""Send POST request"""
import requests
import sys


if __name__ == "__main__":
    session = requests.Session()
    data = {'email': sys.argv[2]}
    response = session.post(sys.argv[1], data=data).text
    print(response)
