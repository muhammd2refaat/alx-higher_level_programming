#!/usr/bin/python3
"""
This Python script that takes 2 arguments in order to solve this challenge.
First argument is the repository name
Second argument is the owner name
You must use the packages requests and sys
"""

import requests
import sys

if __name__ == "__main__":
    url = ('https://api.github.com/repos/{}/{}/commits'
           .format(sys.argv[2], sys.argv[1]))
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
