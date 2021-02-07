import sys

from GuiProperties.GetColumns import *


class MainWindow(QTabWidget):
    def __init__(self, parent=None):
        #super(MainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        self.tabs = QTabWidget()
        self.get_columns = GetColumns()
        self.tab2 = QWidget()
        self.insertTab(0, self.get_columns, "Get Columns")
        #self.insertTab(1, self.tab2, "Set Columns")

        self.setWindowTitle("ExcelProject")
        self.setGeometry(0, 0, 1000, 700)
        self.setStyleSheet("background-color: lightgray;")

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
