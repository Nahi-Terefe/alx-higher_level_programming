#!/usr/bin/python3
"""my body header"""

import urllib.request

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as rep:
        bodyType = rep.read()
        print("Body response:")
        print("\t- type: " + str(type(bodyType)))
        print("\t- content: " + str(bodyType))
        print("\t- utf8 content: " + bodyType.decode('utf-8'))
