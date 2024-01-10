#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    user_email = sys.argv[2]

    value = {'email': user_email}

    # Sending the email parameter to the given the url
    data = urllib.parse.urlencode(value)
    # convert to bytes
    data = data.encode('ascii')

    # To retrieve the data passes to the url
    rep = urllib.request.Request(url, data)

    with urllib.request.urlopen(rep) as response:
        this_output = response.read().decode("utf-8")
        print(this_output)
