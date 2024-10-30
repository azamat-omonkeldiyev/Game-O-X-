from PyQt5.QtWidgets import *
from game_code import Play

class Start_game(QWidget):
    def __init__(self):
        super().__init__()            
        
        self.v_main = QVBoxLayout()
        self.h_btn = QHBoxLayout()
        self.h_edit = QHBoxLayout()
        self.h_edit2 = QHBoxLayout()
        
        self.lbl = QLabel("           Welcome")
        self.lbl.setStyleSheet("font-size: 40px;color:#3A3A63 ;margin-bottom: 30px;font-weight:bold")
        self.lbl2 = QLabel("Player name:")
        self.lbl2.setStyleSheet("font-size: 25px;color:black;margin-bottom: 20px;font-weight:bold")
        self.lbl3 = QLabel("Player2 name:")
        self.lbl3.setStyleSheet("font-size: 25px;color:black;margin-bottom: 20px;font-weight:bold")
        self.edit = QLineEdit()
        self.edit.setStyleSheet("font-size: 25px;color:black;background-color:lightgrey;margin-bottom: 20px;font-weight:bold")
        self.edit2 = QLineEdit()
        self.edit2.setStyleSheet("font-size: 25px;color:black;background-color:lightgrey;margin-bottom: 20px;font-weight:bold")
        self.btn = QPushButton("Exit",clicked = lambda: exit())
        self.btn.setStyleSheet("font-size: 25px;color:white;background-color:#FF7043;margin-bottom: 15px;font-weight:bold")
        self.btn2 = QPushButton("Play",clicked = lambda: self.Chek_player())
        self.btn2.setStyleSheet("font-size: 25px;color:white;background-color:#FF7043;margin-bottom: 15px;font-weight:bold")
        
        self.h_btn.addWidget(self.btn)
        self.h_btn.addWidget(self.btn2)
        self.h_edit.addWidget(self.lbl2)
        self.h_edit.addWidget(self.edit)
        self.h_edit2.addWidget(self.lbl3)
        self.h_edit2.addWidget(self.edit2)
        
        self.v_main.addWidget(self.lbl)
        self.v_main.addLayout(self.h_edit)
        self.v_main.addLayout(self.h_edit2)
        self.v_main.addLayout(self.h_btn)
        
        self.setLayout(self.v_main)
        
    def Chek_player(self):
        if not self.edit.text():
            QMessageBox.warning(self, "Xatolik","Player name kiritilmadi!")
        elif not self.edit2.text():
            QMessageBox.warning(self, "Xatolik","Player2 name kiritilmadi!")
        else:
            self.paly_win = Play(self)
            self.hide()
            self.paly_win.show()
   