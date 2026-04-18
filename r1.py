import requests

# 传参数
params = {
    "name": "qiana",
    "age": 24
}

r = requests.get("https://httpbin.org/get", params=params)

data = r.json()

print("状态码:", r.status_code)
print("返回的URL:", data["url"])
print("服务器收到的参数:", data["args"])