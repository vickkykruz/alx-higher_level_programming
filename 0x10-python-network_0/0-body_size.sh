#!/usr/bin/python3
# Write a Bash script that takes in a URL, sends a request to that URL, and
# displays the size of the body of the r

curl -s "$1" | wc -c
