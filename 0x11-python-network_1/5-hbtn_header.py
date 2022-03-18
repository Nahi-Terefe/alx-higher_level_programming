#!/usr/bin/python3
""" print request id """
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    header = res.headers.get('X-Request-Id')
    print(header)
