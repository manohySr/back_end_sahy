import requests

# set the endpoint URL
url = 'http://localhost:5000/person'

# set the required information for creating a Person object
data = {
    'last_name': 'Doe',
    'first_name': 'John',
    'address': '123 Main St, Anytown USA',
    'email': 'johndoe@example.com',
    'birthday': '1990-01-01',
    'description': 'John Doe is a software engineer.',
    'photo_path': '/path/to/photo',
    'folder_photo_recognition': 'person'
}

# send a POST request to the endpoint with the required information
response = requests.post(url, json=data)

# print the response from the server
print(response.json())
