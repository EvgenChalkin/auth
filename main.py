import sys, random, string
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Auth")

        self.lbl_log = QLabel("login")
        self.edit_log = QLineEdit("user")
        self.lbl_pass = QLabel("password")
        self.edit_pass = QLineEdit("user")
        self.btnAuth = QPushButton("enter")

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_log)
        layout.addWidget(self.edit_log)
        layout.addWidget(self.lbl_pass)
        layout.addWidget(self.edit_pass)
        layout.addWidget(self.btnAuth)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.btnAuth.clicked.connect(lambda: self.auth(self.edit_log.text(), self.edit_pass.text()))

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def auth(self, login, password):
        if login == "user" and password == "user":
            self.window2 = SecondWindow()
            self.window2.show()
            self.close()
        else:
            self.capchaWindow = CapchaWindow()
            self.capchaWindow.show()
            self.close()


class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Test 1")

        self.lbl1 = QLabel("Это тест")
        self.lbl2 = QLabel("вопрос 1, что лишнее?")
        self.rb1 = QRadioButton("тойота")
        self.rb2 = QRadioButton("мазда")
        self.rb3 = QRadioButton("бмв")
        self.btn1 = QPushButton("далее")

        self.btn1.clicked.connect(self.rb)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl1)
        layout.addWidget(self.lbl2)
        layout.addWidget(self.rb1)
        layout.addWidget(self.rb2)
        layout.addWidget(self.rb3)
        layout.addWidget(self.btn1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def rb(self):
        if self.rb3.isChecked():
            self.window4 = TestWindow()
            self.window4.show()
            self.close()


class CapchaWindow(QMainWindow):
    close_ = False

    def closeEvent(self, e):
        if not self.close_:
            e.ignore()

    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Capcha window")

        self.lbl_error = QLabel("Enter capcha: ")
        cap_str = string.digits + string.ascii_lowercase
        cap_list = random.sample(cap_str, 4)
        self.cap_text = ''.join(cap_list)
        self.lbl_cap = QLabel(self.cap_text)
        self.edit_cap = QLineEdit()
        self.btn_cap = QPushButton("enter")
        self.lockout = 0
        self.timeout = 3

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_error)
        layout.addWidget(self.lbl_cap)
        layout.addWidget(self.edit_cap)
        layout.addWidget(self.btn_cap)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.btn_cap.clicked.connect(lambda: self.capcha(self.edit_cap.text(), self.lbl_cap.text()))

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def capcha(self, edit_cap, lbl_rnd):
        if edit_cap == lbl_rnd:
            self.window1 = MainWindow()
            self.close_ = True
            self.window1.show()
            self.close()
        elif self.lockout == 2:
            self.timer = QTimer()
            self.timer.start(1000)
            self.btn_cap.setDisabled(True)
            self.lbl_error.setText("blocked for 3 seconds!")
            self.timer.timeout.connect(self.timer_tick)
        else:
            self.lockout += 1

    def timer_tick(self):
        self.timeout -= 1
        self.lbl_error.setText(f"blocked for {self.timeout} seconds!")
        if self.timeout == 0:
            self.lockout = 0
            self.timeout = 3
            self.timer.stop()
            self.btn_cap.setDisabled(False)
            self.lbl_error.setText("enter capcha: ")


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Test 2")

        self.lbl12 = QLabel("вопрос 2, как зовут на самом деле зовут Кузю из универа?")
        self.rb12 = QRadioButton("Кузя")
        self.rb22 = QRadioButton("Эдик")
        self.rb32 = QRadioButton("Антон")
        self.btn2 = QPushButton("далее")

        self.btn2.clicked.connect(self.rb1)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl12)
        layout.addWidget(self.rb12)
        layout.addWidget(self.rb22)
        layout.addWidget(self.rb32)
        layout.addWidget(self.btn2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def rb1(self):
        if self.rb22.isChecked():
            self.window5 = TestWindow2()
            self.window5.show()
            self.close()


class TestWindow2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Test 3")

        self.lbl13 = QLabel("вопрос 3, кто такой Якубович")
        self.rb13 = QRadioButton("теле-ведущий")
        self.rb23 = QRadioButton("певец")
        self.rb33 = QRadioButton("актер")
        self.btn3 = QPushButton("далее")

        self.btn3.clicked.connect(self.rb2)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl13)
        layout.addWidget(self.rb13)
        layout.addWidget(self.rb23)
        layout.addWidget(self.rb33)
        layout.addWidget(self.btn3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def rb2(self):
        if self.rb13.isChecked():
            self.window6 = TestWindow3()
            self.window6.show()
            self.close()


class TestWindow3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("la finita")

        self.lbl_sweet = QLabel("ТЫ КРАСАВА!")
        self.btn_close = QPushButton("close")
        self.btn_res = QPushButton("view result")

        self.btn_close.clicked.connect(self.close)
        self.btn_res.clicked.connect(self.write_res)

        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        layout.addWidget(self.lbl_sweet)
        hbox.addWidget(self.btn_close)
        hbox.addWidget(self.btn_res)

        widget = QWidget()
        layout.addLayout(hbox)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def write_res(self):
        res = "ТЫ КРАСАВА!"
        with open('res.txt', "w", encoding="utf-8") as f:
            f.write(res)


app = QApplication(sys.argv)
window1 = MainWindow()
window1.show()
app.exec()