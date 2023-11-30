#!/bin/bash
# Write a Bash script that sends a JSON POST displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d "@json_file" "$1"
