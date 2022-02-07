from flask import Flask
import time
from datetime import datetime
from flask import Response, request

app = Flask(__name__)
db = [
            {'text': 'Hello', 'author': 'Anton', 'time': time.time()},
            {'text': 'Привет', 'author': 'Антон', 'time': time.time()},
        ]


@app.route("/")
def hello():
    return "Hello, user!<br><a href='/status'>Статус</a>"


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Together',
        'time': time.time(),
        'time2': time.asctime(),
        'time3': datetime.now(),
    }


@app.route("/send_messages", methods=['POST'])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return Response({'not json'}, 400)

    text = data.get('text')
    author = data.get('author')

    if isinstance(text, str) and isinstance(author, str):
        db.append({
            'text': text,
            'author': author,
            'time': time.time()
        })
        return Response({'ok'})
    else:
        return Response({'wrong format'}, 400)


@app.route("/get_messages")
def get_message():
    after = request.args.get('after', '0')
    try:
        after = float(after)
    except:
        return Response({'wrong format'}, 400)

    new_messages = [m for m in db if m['time'] > after]
    return {'messages': new_messages}


app.run()
