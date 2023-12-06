#!/usr/bin/python3
""" Use requests to query """

if __name__ == '__main__':
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
