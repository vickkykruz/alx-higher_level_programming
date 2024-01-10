#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":

    try:
        q = sys.argv[1]
    except IndexError:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    value = {'q': q}

    response = requests.post(url, value)

    try:
        response_json = response.json()
        valid = True
    except ValueError:
        valid = False
        print("Not a valid JSON")

    if valid:
        if not response_json:
            print("No result")
        else:
            print("[{}] {}".format(
                response_json["id"],
                response_json["name"]))
