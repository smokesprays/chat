import time

import requests
from datetime import datetime

after = 0

while True:
    response = requests.get(
        'http://127.0.0.1:5000/get_messages',
        params={'after': after}
    )
    if response.status_code == 200:
        messages = response.json()['messages']

        for message in messages:
            after = message['time']
            ftime = datetime.fromtimestamp(message['time']).strftime('%d-%m-%y %H:%M:%S')
            print(message['author'], ftime)
            print(message['text'])
            print()

    time.sleep(1)
