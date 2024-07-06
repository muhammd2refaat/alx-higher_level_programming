#!/usr/bin/python3
"""
This Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(username, password)
    )

    try:
        print(response.json().get('id'))
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        print("No result")
