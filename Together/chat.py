from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore
import clientui


class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.pressed.connect(self.send_message)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def get_messages(self):
        try:
            response = requests.get(
                'http://127.0.0.1:5000/get_messages',
                params={'after': self.after}
            )
        except:
            return

        if response.status_code == 200:
            messages = response.json()['messages']

            for message in messages:
                self.after = message['time']
                ftime = datetime.fromtimestamp(message['time']).strftime('%d-%m-%y %H:%M:%S')
                self.textBrowser.append(message['author'] + ' ' + ftime)
                self.textBrowser.append(message['text'])
                #self.textBrowser.append()

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()
        if name and text:
            try:
                response = requests.post(
                    'http://127.0.0.1:5000/send_messages',
                    json={'text': text, 'author': name}
                )
            except:
                self.textBrowser.append('Сервер не доступен')
                self.textBrowser.append('')
                return
        else:
            self.textBrowser.append('Введите ваше имя и сообщение полностью')
            return

        if response.status_code != 200:
            self.textBrowser.append('Ошибка валидации')
            self.textBrowser.append('')
            self.textBrowser.repaint()
            return

        self.textEdit.clear()
        self.textEdit.repaint()


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec_()
