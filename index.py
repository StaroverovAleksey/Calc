import sys
from tkinter import Tk

from UI.ui import *


class MyWin(QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        # QWidget.__init__(self, parent)
        self.ui = Ui_window()
        self.ui.setupUi(self)

        self.inputRadioList = [self.ui.input_radio_1, self.ui.input_radio_2, self.ui.input_radio_3]
        self.outputRadioList = [self.ui.output_radio_1, self.ui.output_radio_2, self.ui.output_radio_3]
        self.ui.button.clicked.connect(self.get_result)
        self.ui.copy_link.clicked.connect(self.copy)
        for radioItem in self.inputRadioList:
            radioItem.clicked.connect(self.clear_output)
        for radioItem in self.outputRadioList:
            radioItem.clicked.connect(self.clear_output)

    def copy(self):
        self.ui.copy_link.setText('Скопировано!')
        self.ui.copy_link.setStyleSheet('QLabel { color : green; }')
        c = Tk()
        c.withdraw()
        c.clipboard_clear()
        c.clipboard_append(self.ui.output.text())
        c.update()
        c.destroy()

    def clear_output(self):
        self.ui.output.setText('')
        self.ui.copy_link.setText('Копировать')
        self.ui.copy_link.setStyleSheet('QLabel { color : blue; }')

    def get_result(self):
        self.ui.output.setText('')
        self.ui.copy_link.setText('Копировать')
        self.ui.copy_link.setStyleSheet('QLabel { color : blue; }')
        inputNotation = 0
        outputNotation = 0
        inputValue = self.ui.input.text()

        for radioItem in self.inputRadioList:
            if radioItem.isChecked():
                inputNotation = int(radioItem.text())

        for radioItem in self.outputRadioList:
            if radioItem.isChecked():
                outputNotation = int(radioItem.text())

        # Из двоичной в десятичную
        if inputNotation == 2 and outputNotation == 10:
            self.ui.output.setText(str(int(inputValue, 2)))

        # Из двоичной в шестнадцатиричную
        if inputNotation == 2 and outputNotation == 16:
            self.ui.output.setText(hex(int(inputValue, 2)))

        # Из десятичной в двоичную
        if inputNotation == 10 and outputNotation == 2:
            self.ui.output.setText(bin(int(inputValue)))

        # Из десятичной в шестнадцатиричную
        if inputNotation == 10 and outputNotation == 16:
            self.ui.output.setText(hex(int(inputValue)))

        # Из шестнадцатиричной в двоичную
        if inputNotation == 16 and outputNotation == 2:
            self.ui.output.setText(bin(int(inputValue, 16)))

        # Из шестнадцатиричной в десятичную
        if inputNotation == 16 and outputNotation == 10:
            self.ui.output.setText(str(int(inputValue, 16)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyWin()
    myApp.show()
    sys.exit(app.exec_())
