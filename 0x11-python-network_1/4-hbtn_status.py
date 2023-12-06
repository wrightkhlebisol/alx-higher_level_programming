#!/usr/bin/python3
""" Use requests to query """
if __name__ == '__main__':
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print(f"""Body response:
- type: {type(response.text)}
- content: {response.text}
""")
