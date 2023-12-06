#!/usr/bin/python3
""" Takes a URL, sends a request to the URL
displays the body of the response
"""
if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    try:
        res = requests.get(url)
        print(res.text)
    except requests.exception.HTTPError as e:
        if e >= 400:
            print(f"Error code: {e.errno}")
