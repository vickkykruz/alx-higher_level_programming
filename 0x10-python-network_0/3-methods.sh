#!/bin/bash
# Write a Bash script that displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | grep -E "Allow: " | cut -d " " -f 2-
