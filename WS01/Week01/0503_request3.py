import requests


if __name__ == "__main__":
    url = "http://python123.io/ws"
    kv = {'key1': 'value1', 'key2': 'value2'}
    r = requests.request('POST', url, json=kv)
    print(r.text)

# console
# https://python123.io/ws?key1=value1&key2=value2