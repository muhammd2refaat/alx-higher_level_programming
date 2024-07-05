#!/bin/bash
# This script will send a POST request to the URL passed as the first argument and display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
