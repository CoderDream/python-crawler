import requests


if __name__ == "__main__":
    url = "http://python123.io/ws"
    hd = {'user-agent': 'Chrome/10'}
    r = requests.request('POST', url, headers=hd)
    print(r.text)

# console
# https://python123.io/ws?key1=value1&key2=value2