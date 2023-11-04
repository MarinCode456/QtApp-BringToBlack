import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5 import uic

class main_window(QWidget):
    timer = QTimer()

    # Значения, отвечающие за изменение цвета
    r, g, b = 255, 255, 255
    # Все виды монет
    r_coin, g_coin, b_coin = 0, 0, 0
    # Улучшения для каждого цвета
    r_upgrade, g_upgrade, b_upgrade = 0, 0, 0

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Color Change")
        self.setFixedHeight(600)
        self.setFixedWidth(600)

        # Таймер, который каждую секунду меняет значение монет
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.add_coins)
        self.timer.start()

        layout = QGridLayout()
        self.setLayout(layout)

        # Лейблы для отображения значения монет
        r_label = QLabel("0")
        g_label = QLabel("0")
        b_label = QLabel("0")
        #layout.addWidget(r_label, 0, 0, Qt.AlignmentFlag.AlignTop)
        #layout.addWidget(g_label, 0, 1, Qt.AlignmentFlag.AlignTop)
        #layout.addWidget(b_label, 0, 2, Qt.AlignmentFlag.AlignTop)

        button = QPushButton("bring in to black")
        button.setFixedHeight(50)
        button.setFixedWidth(150)
        button.clicked.connect(self.button_change_color)
        #layout.addWidget(button, 0, 1, Qt.AlignmentFlag.AlignCenter)
    
    def button_change_color(self):
        # Округляем каждое значение монет, так как Python особенный
        self.r_coin = round(self.r_coin + 0.1, 1)
        self.g_coin = round(self.g_coin + 0.1, 1)
        self.b_coin = round(self.b_coin + 0.1, 1)
        print(self.r_coin, self.b_coin, self.g_coin)

    def add_coins(self):
        print("+1 монета")

app = QApplication(sys.argv)

screen = main_window()
screen.show()

sys.exit(app.exec_())