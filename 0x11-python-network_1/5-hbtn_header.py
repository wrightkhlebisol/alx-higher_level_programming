#!/usr/bin/python3
"""Takes URL, sends a request to the URL and diplays the
value of the variable X-Request-Id in the response header"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
