import requests


if __name__ == "__main__":
    url = "http://httpbin.org/post"
    r = requests.post(url, data='ABC ') # 向URL POST一个字典自动编码为data
    print(r.text)

# console:
# {
#   "args": {},
#   "data": "ABC ",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "4",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.23.0",
#     "X-Amzn-Trace-Id": "Root=1-5ea286d6-999907e4ca945807d9218f0e"
#   },
#   "json": null,
#   "origin": "27.17.34.234",
#   "url": "http://httpbin.org/post"
# }