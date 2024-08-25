import requests
# response = requests.get("http://192.168.1.102:80/person")
# person = response.json()
# print(person["name"])

# now we are gonna make a token as a password so you can only access this data with the right password!!
response = requests.get("http://192.168.1.102:80/person?token=abc123")
person = response.json()
print(person["name"])