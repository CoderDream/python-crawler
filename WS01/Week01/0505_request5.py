import requests


if __name__ == "__main__":
    url = "http://python123.io/ws"
    fs = {'file': open('data.xls', 'rb')}
    r = requests.request('POST', url, files=fs)
    print(r.text)

# console