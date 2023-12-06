#!/usr/bin/python3
""" Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """

if __name__ == '__main__':
    import sys
    import requests
    username = sys.argv[1]
    pa_token = sys.argv[2]
    gith_url = f"https://api.github.com/user"
    headers = {
        'Authorization': f"Bearer {pa_token}",
        "Accept": "application/vnd.github+json"
    }
    res = requests.get(gith_url, headers=headers)
    try:
        j_res = res.json()

        if j_res.get('id'):
            print(j_res.get('id'))
        else:
            print(None)
    except Exception as e:
        print(None)
