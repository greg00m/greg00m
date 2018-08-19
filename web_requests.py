#!/usr/bin/python3

import requests

r = requests.get('http://www.google.com/search', params={'q': 'test'})

print("Web site text.")
print(r.text)
print("Web response status code")
print(r.status_code)
print("Web site directory headings")
print(dir(r))

s = requests.post('https://pastebin.com/search', data={'item1': 'hello', 'item2': 'world'})

#print("Web site text.")
#print(s.text)
#print("Web response status code")
#print(s.status_code)
#print("Web site directory headings")
#print(dir(s))


