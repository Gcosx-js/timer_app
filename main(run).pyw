from PyQt5.QtWidgets import *
from timer import Ui_Form
from PyQt5.QtCore import QTimer
import ctypes


class timer_screen(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.timer = Ui_Form()
        self.timer.setupUi(self)
        self.timer.saat.setPlaceholderText("0")
        self.timer.deqiqe.setPlaceholderText("0")
        self.timer.saniye.setPlaceholderText("0")
        self.timer.basla.clicked.connect(self.basla)
        self.timer_vaxt = QTimer(self)
        self.timer_vaxt.timeout.connect(self.geri_say)

    def basla(self):
        try:
            saat = int(self.timer.saat.text()) if self.timer.saat.text() != '' else 0
            dk = int(self.timer.deqiqe.text()) if self.timer.deqiqe.text() != '' else 0
            san = int(self.timer.saniye.text()) if self.timer.saniye.text() != '' else 0
            self.h = (saat*3600)+(dk*60)+san
            self.geri_say()
            self.timer_vaxt.start(1000)
        except ValueError:
            ctypes.windll.user32.MessageBoxW(0, "Xəta Baş Verdi!\nZəhmət olmasa tam rəqəm daxil etdiyinizdən əmin olun!", "Timer Error", 0x10)

    def geri_say(self):
        if self.h > 0:
            saat = self.h // 3600
            dk = (self.h % 3600) // 60
            san = self.h % 60
            self.vaxt = "{:02d}:{:02d}:{:02d}".format(saat, dk, san)
            self.timer.label_4.setText(str(self.vaxt))
            self.h -= 1
        else:
            self.timer_vaxt.stop()
app = QApplication([])
ekran = timer_screen()
ekran.show()
app.exec_()
