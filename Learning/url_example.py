from urllib.request import urlopen
response = urlopen("http://httpbin.org/html")

contents = response.read()
print(response.status)
html = contents.decode("utf-8")
print(html[:400])