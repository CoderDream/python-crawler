import requests


if __name__ == "__main__":
    url = "http://python123.io/ws"
    kv = {'key1': 'value1', 'key2': 'value2'}
    r = requests.request('GET', url, params=kv)
    print(r.url)

# console
# https://python123.io/ws?key1=value1&key2=value2