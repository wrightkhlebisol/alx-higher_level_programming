#!/usr/bin/python3
""" Send a POST request to the passed URL with email as param """
if __name__ == '__main__':
    import urllib.request
    import sys
    url = sys.argv[1]
    body = {
        'email': sys.argv[2]
    }
    with urllib.request.urlopen(url, body) as response:
        print(response.read().decode('utf-8'))
