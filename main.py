import sys
import random

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
from PyQt5 import uic

class App(QMainWindow):
    timer = QTimer()
    end_timer = QTimer()

    # Все виды монет
    r_coin, g_coin, b_coin = 0, 0, 0
    # Улучшения для каждого цвета
    r_upgrade, g_upgrade, b_upgrade = 255, 255, 254
    r_upg_cost, g_upg_cost, b_upg_cost = 10, 10, 10
    # Рандомные надписи для главной кнопки
    random_text = ["bring to black", "oh, nice click", "meow", "so strange", "megadeth",
                   "more green!", "selmash", "welcome to the club", "bring to black", "bring to white"]

    def __init__(self):
        # Загружаем интерфейс из QtDesigner
        super().__init__()
        uic.loadUi("program.ui", self)

        # Таймер, который каждую секунду меняет значение монет
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.add_coins)
        self.timer.start()

        # Таймер, который проверяет дошли ли мы до чёрного
        self.end_timer.setInterval(5000)
        self.end_timer.timeout.connect(self.check_end)
        self.end_timer.start()

        # Место задания функций для каждой кнопки
        self.main_button.clicked.connect(self.button_change_color)
        self.mred_button.clicked.connect(self.red_up)
        self.mgreen_button.clicked.connect(self.green_up)
        self.mblue_button.clicked.connect(self.blue_up)
    
    def button_change_color(self):
        # Чтобы при каждом клике был новый текст у кнопки
        choice = random.choice(self.random_text)
        while choice == self.main_button.text():
            choice = random.choice(self.random_text)
        self.main_button.setText(choice)

        match random.randint(0,2):
            case 0: 
                self.r_coin += 1
                self.red_count.setText(str(self.r_coin))
            case 1: 
                self.g_coin += 1
                self.green_count.setText(str(self.g_coin))
            case 2: 
                self.b_coin += 1
                self.blue_count.setText(str(self.b_coin))

    # Срабатывает раз в секунду и добавляет монеты
    def add_coins(self):
        self.r_coin += self.r_upgrade
        self.g_coin += self.g_upgrade
        self.b_coin += self.b_upgrade

        self.red_count.setText(str(self.r_coin))
        self.green_count.setText(str(self.g_coin))
        self.blue_count.setText(str(self.b_coin))

    # Проверяем дошли ли мы до чёрного
    # Если достигли, просто меняем цвет кнопки и текста
    def check_end(self):
        if (self.r_upgrade == 255) and (self.g_upgrade == 255) and (self.b_upgrade == 255):
            self.main_button.setStyleSheet("background-color: gold; color: black;")

    def red_up(self):
        if (self.r_coin >= self.r_upg_cost) and self.r_upgrade != 255:
            self.r_upgrade += 1
            self.r_coin -= self.r_upg_cost
            self.r_upg_cost += 10

            self.red_count.setText(str(self.r_coin))
            self.red_upgrade.setText("+" + str(self.r_upgrade))
            self.r_upg_cost_label.setText("upgrade cost: " + str(self.r_upg_cost))

            self.reload_back()
    def green_up(self):
        if (self.g_coin >= self.g_upg_cost) and self.g_upgrade != 255:
            self.g_upgrade += 1
            self.g_coin -= self.g_upg_cost
            self.g_upg_cost += 10

            self.green_count.setText(str(self.g_coin))
            self.green_upgrade.setText("+" + str(self.g_upgrade))
            self.g_upg_cost_label.setText("upgrade cost: " + str(self.g_upg_cost))

            self.reload_back()
    def blue_up(self):
        if (self.b_coin >= self.b_upg_cost) and self.b_upgrade != 255:
            self.b_upgrade += 1
            self.b_coin -= self.b_upg_cost
            self.b_upg_cost += 10

            self.blue_count.setText(str(self.b_coin))
            self.blue_upgrade.setText("+" + str(self.b_upgrade))
            self.b_upg_cost_label.setText("upgrade cost: " + str(self.b_upg_cost))

            self.reload_back()

    # Меняем цвет фона
    def reload_back(self):
        styleStr = f"background-color: rgb({255-self.r_upgrade}, {255-self.g_upgrade}, {255-self.b_upgrade})"
        self.background.setStyleSheet(styleStr)

app = QApplication(sys.argv)

prog = App()
prog.show()

sys.exit(app.exec_())