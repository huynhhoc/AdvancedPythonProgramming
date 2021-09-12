import urllib.request
req = urllib.request.Request('http://www.python.org/fish.html')
try:
   urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
  print(e.code)
  print(e.read())
