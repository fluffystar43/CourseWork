from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QMessageBox
from PyQt5 import uic
import sys
from enum import Enum

class Operation(Enum):
    plus = 1
    minus = 2
    mul = 3
    div = 4
    power = 5

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calculator.ui', self)
        self.initUI()        
        
    def initUI(self):
        self.center()
        self.pbPlus.clicked.connect(lambda: self.calculate(Operation.plus.value))
        self.pbMinus.clicked.connect(lambda: self.calculate(Operation.minus.value))
        self.pbMulti.clicked.connect(lambda: self.calculate(Operation.mul.value))
        self.pbDiv.clicked.connect(lambda: self.calculate(Operation.div.value))
        self.pbExponentation.clicked.connect(lambda: self.calculate(Operation.power.value))
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())        
    
    def calculate(self, Enum):
        try:
            x = float(self.textEditFirst.toPlainText())
            y = float(self.textEditSecond.toPlainText())
            if (Enum == 1): self.textEditResult.setText(str(x+y))
            elif (Enum == 2): self.textEditResult.setText(str(x-y))
            elif (Enum == 3): self.textEditResult.setText(str(x*y))
            elif (Enum == 4): self.textEditResult.setText(str(x/y))
            elif (Enum == 5): self.textEditResult.setText(str(x**y))
        except:
            QMessageBox.information(self, 'Ошибка', 'Неверные данные')
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())