#!/bin/bash
# Write a Bash script that takes in a URLand displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
