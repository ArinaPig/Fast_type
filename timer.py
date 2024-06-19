from datetime import datetime

self.button_start = QtWidgets.QPushButton(self.lvl_1)
self.button_start.setGeometry(QtCore.QRect(700, 75, 100, 30))
self.button_start.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 10px;\n"
                                 "font: 15pt \"Roboto\";")
self.button_start1.setObjectName("button_start")
self.button_start1.clicked.connect(self.func_start)

self.temp = 0

timer = QtCore.QTimer()
self.timer.setInterval(1000)
self.timer.timeout.connect(self.displayTime1)


def func_start(self):
    if self.button_start.text() == 'Старт':
        self.timer1.start()
        self.button_start1.setText('Стоп')
    else:
        self.timer1.stop()
        self.button_start1.setText('Старт')
        self.button_start1.hide()

def displayTime(self):
    f_temp = datetime.utcfromtimestamp(self.temp).strftime("%M:%S")
    self.label_4.setText(f_temp)
    self.temp += 1