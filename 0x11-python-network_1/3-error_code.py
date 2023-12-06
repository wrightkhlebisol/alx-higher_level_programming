#!/usr/bin/python3
""" Takes a URL, sends a request and displays response body in utf-8 """
if __name__ == '__main__':
    import sys
    import urllib.request
    path = sys.argv[1]
    try:
        with urllib.request.urlopen(path) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.getcode}")
