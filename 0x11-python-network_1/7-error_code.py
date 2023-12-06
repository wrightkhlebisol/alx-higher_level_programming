#!/usr/bin/python3
""" Takes a URL, sends a request to the URL
displays the body of the response
"""
if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
