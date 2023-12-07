#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""

if __name__ == '__main__':
    import sys
    import requests
    REPO = sys.argv[1]
    OWNER = sys.argv[2]
    gith_url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    payload = {'per_page': '10', 'page': '1'}
    res = requests.get(gith_url, params=payload)
    try:
        if len(res.json()) > 0:
            for r in res.json():
                print(f"{r.get('sha')}: {r.get('commit')['author']['name']}")
        else:
            print(None)
    except Exception as e:
        print(None, e)
