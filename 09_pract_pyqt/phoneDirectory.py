from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('phoneDirectory.ui', self)
        self.initUI() 
    
    def initUI(self):
        self.center()
        self.pushButtonAdd.clicked.connect(self.addToTabble)        
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft()) 
        
    def addToTabble(self):
        try:
            rows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rows)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(self.lineEditFirst.text()))
            self.tableWidget.setItem(rows, 1, QTableWidgetItem(self.lineEditSecond.text()))
            QMessageBox.information(self, 'Выполнено', 'Данные добавлены в таблицу')
        except Exception:
            QMessageBox.information(self, 'Ошибка', 'Неверные данные')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())