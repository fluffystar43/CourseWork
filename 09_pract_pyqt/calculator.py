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
        self.pbPlus.clicked.connect(lambda: self.calculate(Operation.plus))
        self.pbMinus.clicked.connect(lambda: self.calculate(Operation.minus))
        self.pbMulti.clicked.connect(lambda: self.calculate(Operation.mul))
        self.pbDiv.clicked.connect(lambda: self.calculate(Operation.div))
        self.pbExponentation.clicked.connect(lambda: self.calculate(Operation.power))
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())        
    
    def calculate(self, operation):
        try:
            x = float(self.textEditFirst.toPlainText())
            y = float(self.textEditSecond.toPlainText())
            if (operation == Operation.plus): result = (str(x+y))
            elif (operation == Operation.minus): result = (str(x-y))
            elif (operation == Operation.mul): result = (str(x*y))
            elif (operation == Operation.div): result = (str(x/y))
            elif (operation == Operation.power): result = (str(x**y))
            self.textEditResult.setText(result)
        except:
            QMessageBox.information(self, 'Ошибка', 'Неверные данные')
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())