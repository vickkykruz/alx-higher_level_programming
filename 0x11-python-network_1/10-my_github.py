#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id

    => You must use Basic Authentication with a personal access token as
        password to access to your information (only read:user permission
        is needed)
    => The first argument will be your username
    => The second argument will be your password (in your case, a personal
        access token as password)
    => You must use the package requests and sys
    => You are not allowed to import packages other than requests and sys
"""

import requests
import sys


if __name__ == "__main__":

    url = "https://api.github.com/user"
    header = {
            "Authorization": "Bearer {}".format(sys.argv[2]),
            "X-GitHub-Api-Version": "2022-11-28"}

    response = requests.get(url, headers=header)

    try:
        print(response.json()["id"])
    except KeyError:
        print(None)
