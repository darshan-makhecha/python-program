import urllib.request
fid=urllib.request.urlopen('http://www.example.org/')
webpage=fid.read().decode('utf-8')
print(webpage)
