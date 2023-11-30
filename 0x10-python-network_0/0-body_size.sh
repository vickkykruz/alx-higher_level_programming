#!/bin/bash
# Write a Bash script that takes in a URL, displays the size of the body
curl -s "$1" | wc -c
