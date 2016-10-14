import urllib.request
import urllib.error

req = urllib.request.Request('http://www.ython.org/fish.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
    print("MyWeeror") 
