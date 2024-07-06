#!/usr/bin/python3
"""
This Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as response:
        content_response = response.text
        print("Body response:")
        print(f"\t- type: {type(content_response)}")
        print(f"\t- content: {content_response}")
