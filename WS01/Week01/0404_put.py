import requests


if __name__ == "__main__":
    url = "http://httpbin.org/put"
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.put(url, data=payload) # 向URL POST一个字典自动编码为form（表单）
    print(r.text)

# console:
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "23",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.23.0",
#     "X-Amzn-Trace-Id": "Root=1-5ea2872c-46ae75228099a7f2429d1554"
#   },
#   "json": null,
#   "origin": "27.17.34.234",
#   "url": "http://httpbin.org/put"
# }