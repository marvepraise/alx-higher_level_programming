#!/usr/bin/python3
"""List 10 commits"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    session = requests.Session()
    response = session.get(url)
    r = response.json()
    i = 0
    for commit in r:
        if i < 10:
            print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit').get('author')
                                  .get('name')))
        i += 1
