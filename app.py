from PyQt5.QtWidgets import *

class searchWindow(QWidget):
    def __init__(self,obj):
        super().__init__()
        self.setStyleSheet('font-size:20px')
        self.main_window=obj

        self.v_main_lay=QVBoxLayout()
        self.h_rd_lay=QHBoxLayout()
        self.h_eb_lay=QHBoxLayout()
        self.h_btn_lay=QHBoxLayout()

        self.rd1=QRadioButton('Uzb')
        self.rd2=QRadioButton('Eng')
        self.search_edit=QLineEdit()
        self.search_btn=QPushButton('Search')
        self.search_btn.clicked.connect(self.search_word)
        self.lbl=QLabel()
        self.menu_btn=QPushButton('MENU')
        self.menu_btn.clicked.connect(self.menu)
        self.add_btn=QPushButton('Add')
        self.add_btn.hide()
        self.add_btn.clicked.connect(self.add)

        self.h_rd_lay.addWidget(self.rd1)
        self.h_rd_lay.addWidget(self.rd2)
        self.h_eb_lay.addWidget(self.search_edit)
        self.h_eb_lay.addWidget(self.search_btn)
        self.h_btn_lay.addWidget(self.menu_btn)
        self.h_btn_lay.addWidget(self.add_btn)
        self.v_main_lay.addLayout(self.h_rd_lay)
        self.v_main_lay.addLayout(self.h_eb_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h_btn_lay)
        self.setLayout(self.v_main_lay)
    
    def add(self):
        self.hide()
        self.main_window.Add()
    def menu(self):
        self.hide()
        self.main_window.show()
    def search_word(self):
        if self.rd1.isChecked() or self.rd2.isChecked():
            if self.search_edit.text():
                if self.rd1.isChecked():
                    f=open('lugat.txt')
                    f.seek(0)
                    lamp=0
                    for i in f.readlines():
                        if self.search_edit.text()==i.split('-')[0]:
                            self.lbl.setText(f"{i.split('-')[1]}")
                            lamp=1
                    if lamp!=1:
                        self.lbl.setText('Bunday soz yoq')
                        self.add_btn.show()
                else:
                    f=open('lugat.txt')
                    f.seek(0)
                    lamp=0
                    for i in f.read().split('\n'):
                        if self.search_edit.text()==i.split('-')[-1]:
                            self.lbl.setText(f"{i.split('-')[0]}")
                            lamp=1
                    if lamp!=1:
                        self.lbl.setText('Bunday soz yoq')
                        self.add_btn.show()
            else:
                self.lbl.setText('soz kiriting')
        else:
            self.lbl.setText('biron bir til ni tanlang!!!')
