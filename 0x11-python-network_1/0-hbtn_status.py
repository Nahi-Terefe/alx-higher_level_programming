#!/usr/bin/python3
"""my body header"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rep:
        print("Body response:")
        bodyType = rep.read()
        print("\t- type: {}".format(type(rep.read())))
        print("\t- content: {}".format(bodyType))
        print("\t- utf8 content: {}".format(bodyType.decode('utf-8')))
