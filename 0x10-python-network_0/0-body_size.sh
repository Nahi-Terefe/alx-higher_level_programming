#!/bin/bash
# requests and displays response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
