#!/usr/bin/python3
"""my body header"""

import urllib.request

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen() as rep:
        bodyType = rep.read()
        print("Body response:")
        print("\t- type: {}".format(type(bodyType)))
        print("\t- content: {}".format(bodyType))
        print("\t- utf8 content: {}".format(bodyType.decode('utf-8')))
