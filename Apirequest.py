import requests
def abcs():
    print("hello woird")

abcs()

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.status_code)
print(response.json())

# assert response.status_code==200

if response.status_code==200:
    print("its working")
else:
    print("not wporking")