import time


class Chat:
    def __init__(self):
        self.db = [
            {'text': 'Привет', 'Author': 'anton', 'time': time.time()}
        ]

    def send_message(self, text, author):
        if isinstance(text,str) and isinstance(author,str):
            self.db.append({
                'text': text,
                'author': author,
                'time': time.time()
            })
            print(text, author)
            return 'Ok'
        else:
            return 'Not Ok'
    def get_message(self):
        return self.db


m = Chat()
m.send_message('Hi','Jana')
print(m.get_message())
