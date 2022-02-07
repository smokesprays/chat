import requests

response = requests.post(
    'http://127.0.0.1:5000/send_messages',
    json={'text': 'Hi', 'author': 'X'}
)
print(response.status_code)
print(response.text)
