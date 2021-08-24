import urllib.request
with urllib.request.urlopen('https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages ') as response:
   html = response.read()
with open('message.txt', 'wb') as file:
    file.write(html)
print('done')
