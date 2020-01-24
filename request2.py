from urllib import request

response = request.urlopen('http://www.python.org')
i=0
while i<10:
    for line in response:
        print(line,' ',i)
        i+=1
        break
