import urllib.request

webUrl = urllib.request.urlopen('https://www.google.in')
print("result code " + str(webUrl.getcode()))

data = webUrl.read() 
print (data )
