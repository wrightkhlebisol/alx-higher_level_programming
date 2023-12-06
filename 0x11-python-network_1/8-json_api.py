#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the
    letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1]
    if not q:
        q = ''
    body = {'q': q}
    res = requests.post(url, data=body)
    if res:
        print(f"[{res.id}] {res.name}")
    else:
        print("No result")
