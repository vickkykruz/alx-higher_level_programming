#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of the
response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    rep = urllib.request.Request(url)

    with urllib.request.urlopen(rep) as response:
        this_output = response.info()
        print('{}'.format(this_output['X-Request-Id']))
