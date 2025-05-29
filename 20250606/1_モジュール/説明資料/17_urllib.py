import urllib.request
import ssl

url = "https://jsonplaceholder.typicode.com/posts"

context = ssl._create_unverified_context()

response = urllib.request.urlopen(url, context=context)

print(response.read())
