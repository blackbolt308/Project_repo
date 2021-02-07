from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
import pandas as pd


class GetColumns(QTabWidget):
    def __init__(self):
        QTabWidget.__init__(self)
        self.label_names = {}
        self.tab1 = QWidget()
        self.hlayout = QHBoxLayout()
        self.vlayout = QVBoxLayout(self.tab1)
        self.labels = QLabel(self)
        self.col_dic = dict()
        self.tab1.setLayout(self.hlayout)
        self.file_name_text_box = QLineEdit(self)
        self.file_name_label = QLabel(self)
        self.column_name_label = QLabel(self)
        self.open_browser_button = QPushButton('Browse', self)
        self.file_selection_options = QFileDialog.Options()
        self.column_names = []
        self._set_dimensions_()

    def _set_dimensions_(self):
        self.open_file_label()
        self.file_name_text()
        self.open_file_button()
        self.file_load_button()
        self.set_column_labels_text(self.column_names)

    def get_column_name(self, filename):
        df = pd.read_excel(filename)
        self.get_col_info(df.columns)
        for val in df.columns:
            self.column_names.append(val)

        print(self.column_names)
        self.set_column_labels_text(self.column_names)

    def set_column_labels_text(self, col_names):
        font = QFont()
        font.setPointSize(12)
        label_x_axis = 40
        label_y_axis = 100
        text_x_axis = 300
        text_y_axis = 100
        for val in col_names:
            label = QLabel(self)
            label.setGeometry(QRect(label_x_axis, label_y_axis, 350, 40))
            label.setFont(font)
            label.setText(val)
            text_box = QLineEdit(self)
            text_box.setGeometry(QRect(text_x_axis, text_y_axis, 350, 40))
            text_box.setStyleSheet("background-color: white;")
            label_y_axis += 50
            text_y_axis += 50


    def open_file_label(self):
        font = QFont()
        font.setPointSize(14)
        self.file_name_label.setFont(font)
        self.file_name_label.setGeometry(40, 50, 100, 40)
        self.file_name_label.setText("File Name")

    def file_name_text(self):
        self.file_name_text_box.setGeometry(QRect(300, 50, 400, 40))
        self.file_name_text_box.setStyleSheet("background-color: white;")

    def open_file_button(self):
        self.open_browser_button.move(750, 45)
        self.open_browser_button.resize(100, 50)
        self.open_browser_button.clicked.connect(self.open_file_name_dialog)
        #self.file_name_text_box.setText(file_name)

    def file_load_button(self):
        self.file_load_button = QPushButton('Load File', self)
        self.file_load_button.move(875, 45)
        self.file_load_button.resize(100, 50)
        #self.file_load_button.clicked.connect(self.set_column_labels)

    def open_file_name_dialog(self):
        self.file_selection_options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Browse Excel File", "","All Files (*);;Excel Files (*.xlsx)", options=self.file_selection_options)
        if fileName:
            #self.column_names.clear()
            self.file_name_text_box.setText(fileName)
            self.get_column_name(fileName)
        else:
            pass




