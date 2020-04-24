import requests


if __name__ == "__main__":
    url = "http://python123.io/ws"
    pxs = {'http': 'http://user:pass@10.10.10.1:1234',
            'https': 'https://10.10.10.1:4321'}
    r = requests.request('POST', url, proxies=pxs)
    print(r.text)

# console