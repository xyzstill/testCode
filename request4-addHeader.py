from urllib import request

req=request.Request('http://bing.com')
req.add_header('Use-agent',
               'PyMOTW(https://pymotw.com/')

response=request.urlopen(req)
data=response.read().decode('utf-8')
print(data)
