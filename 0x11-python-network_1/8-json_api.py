#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the
    letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ''
    body = {'q': q}
    res = requests.post(url, data=body)
    try:
        j_res = res.json()
        if j_res:
            print(f"[{j_res.get('id')}] {j_res.get('name')}")
        elif len(j_res) <= 0:
            print("No result")
    except requests.JSONDecodeError as e:
        print("Not a valid JSON")
