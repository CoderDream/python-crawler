import requests


if __name__ == "__main__":
    url = "http://httpbin.org/get"
    r = requests.head(url)
    print(r.headers)
