#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    rep = urllib.request.Request(url)

    with urllib.request.urlopen(rep) as response:
        this_output = response.read()

        print('Body response:')
        print('\t - type: {}'.format(type(this_output)))
        print('\t - content: {}'.format(this_output))
        print('\t -utf8 content: {}'.format(this_output.decode("utf-8")))
