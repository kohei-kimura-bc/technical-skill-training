import requests


response = requests.get("https://jsonplaceholder.typicode.com/posts", verify=False)
print(response.text)
