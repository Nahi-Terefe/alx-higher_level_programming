#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository and user
sent in as arguments
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = "https://api.github.com/repos/{}/{}/commits"
    res = requests.get(url.format(argv[2], argv[1]))
    commits = res.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
