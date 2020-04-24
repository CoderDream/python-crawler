import requests


if __name__ == "__main__":
    url = "http://python123.io/ws"
    r = requests.request('POST', url, timeout=10)
    print(r.text)

# console