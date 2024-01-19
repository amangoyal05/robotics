import requests

r = requests.get('https://xkcd.com/353/')
# print(help(r))
# print(r.text)

r1 = requests.get('https://imgs.xkcd.com/comics/python.png')

# with open("comic.png", "wb") as f:
#     f.write(r1.content)

# 200 - Success
# 300 - Redirects
# 400 - Client Error. For eg, accessing a page to which we do not have access to.
# 500 - Server Error. Site crashes and we can not access it for sometime.
print(r.status_code)
print(r.ok)                 # Will return True for anything less than 400, ie, no error with accessing the website
print(r.headers)


payload = {'username': 'Aman', 'password': 'testing'}
r2 = requests.get('https://httpbin.org/get', params = payload)

print(r2.url)

r2 = requests.post('https://httpbin.org/post', data = payload)
r_dict = r2.json()
print(r2.json())
print(r_dict['form'])


r2 = requests.get('https://httpbin.org/basic-auth/aman/testing', auth = ('aman', 'testing'))
print(r2.text)

r2 = requests.get('https://httpbin.org/basic-auth/aman/testing', auth = ('amangoyal', 'testing'))
print(r2.text)
print(r2)

r2 = requests.get('https://httpbin.org/basic-auth/aman/testing', 
                  auth = ('aman', 'testing'), timeout=3)
print(r2.text)