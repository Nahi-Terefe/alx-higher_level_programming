#!/usr/bin/python3
""" print error code """
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    try:
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(res.status_code))
