from PyQt5.QtWidgets import *

class Play(QWidget):
    def __init__(self,obj):
        super().__init__()
        
        self.obj = obj
        self.ism = obj.edit.text()
        self.ism2 = obj.edit2.text()
        
        self.grid_lay =QGridLayout()
        self.v_main_lay = QVBoxLayout()
        self.h_lay = QHBoxLayout()
        
        self.btn = QPushButton("Start",clicked = lambda: self.Start())
        self.btn.setStyleSheet("font-size: 25px;color : white;background-color:#00FF00;margin-bottom: 30px;font-weight:bold")
        self.btn3 = QPushButton("Davom etish",clicked = lambda: self.Davom_etish())
        self.btn3.setStyleSheet("font-size: 25px;color : white;background-color:#00FF00;margin-bottom: 30px;font-weight:bold")
        self.btn3.hide()
        self.btn2 = QPushButton("Exit",clicked = lambda: self.Exit())
        self.btn2.setStyleSheet("font-size: 25px;color : white;background-color: #0000FF;margin-bottom: 30px;font-weight:bold")
        
        self.lbl = QLabel(f"Hisob: |{self.ism}| 0 - 0 |{self.ism2}|")
        self.lbl.setStyleSheet("font-size: 25px;color:#AD1457 ;margin-bottom: 30px;font-weight:bold")
        self.lbl2 = QLabel(f"O'yinni {self.ism} boshlaydi!")
        self.lbl2.setStyleSheet("font-size: 25px;color:black ;margin-bottom: 30px;font-weight:bold")
        self.lbl2.hide()
        
        self.son = 1
        self.count = 0
        
        index = 0
        self.lst_kataklar = []
        for i in range(3):
            for j in range(3):
                katak = QPushButton(' ', clicked=lambda _, x=index: self.Playing(x))
                katak.setStyleSheet("font-size : 30px") 
                self.lst_kataklar.append(katak)
                self.lst_kataklar[index].setEnabled(False)
                self.grid_lay.addWidget(katak,i,j)
                index += 1
        
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.grid_lay)
        self.v_main_lay.addWidget(self.lbl2)
        self.h_lay.addWidget(self.btn2)
        self.h_lay.addWidget(self.btn)
        self.h_lay.addWidget(self.btn3)
        
        self.v_main_lay.addLayout(self.h_lay)
        self.setLayout(self.v_main_lay)
        
    def Playing(self,index):
        if self.son % 2 == 1:
            self.lst_kataklar[index].setText("X")
            self.lst_kataklar[index].setStyleSheet("font-size: 30px ;color : red")
            self.lst_kataklar[index].setEnabled(False)
            self.son += 1
            self.lbl2.setText(f"{self.ism2}ning navbati..")
            self.Chek_game(self.ism)
        else:
            self.lst_kataklar[index].setText("O")
            self.lst_kataklar[index].setStyleSheet("font-size : 30px; color : green")
            self.lst_kataklar[index].setEnabled(False)
            self.son += 1
            self.lbl2.setText(f"{self.ism}ning navbati..")
            self.Chek_game(self.ism2)
            
    def Chek_game(self,user):
        x = self.lst_kataklar
        self.count += 1
        if x[0].text() == x[1].text() and x[0].text() == x[2].text() and x[0].text() != ' ':
            self.Stop(user)
            QMessageBox.information(self, "Winner",f"{user} is winner!")
        if x[3].text() == x[4].text() and x[3].text() == x[5].text() and x[3].text() != ' ':
            self.Stop(user)
            QMessageBox.information(self, "Winner",f"{user} is winner!")
        if x[6].text() == x[7].text() and x[6].text() == x[8].text() and x[6].text() != ' ':
            self.Stop(user)
            QMessageBox.information(self, "Winner",f"{user} is winner!")
        if x[0].text() == x[3].text() and x[0].text() == x[6].text() and x[0].text() != ' ':
            self.Stop(user)
            QMessageBox.information(self, "Winner",f"{user} is winner!")
        if x[1].text() == x[4].text() and x[1].text() == x[7].text() and x[1].text() != ' ':
            self.Stop(user)
            QMessageBox.information(self, "Winner",f"{user} is winner!")
        if x[2].text() == x[5].text() and x[2].text() == x[8].text() and x[2].text() != ' ':
            self.Stop(user)
            QMessageBox.information(self, "Winner",f"{user} is winner!")
        if x[0].text() == x[4].text() and x[0].text() == x[8].text() and x[0].text() != ' ':
            self.Stop(user)
            QMessageBox.information(self, "Winner",f"{user} is winner!")
        if x[2].text() == x[6].text() and x[2].text() == x[4].text() and x[2].text() != ' ':
            self.Stop(user)
            QMessageBox.information(self, "Winner",f"{user} is winner!")
        if self.count == 9:    
            self.Stop(2)
            QMessageBox.information(self, "Winner",f"Do'stlik g'alaba qozondi!")
         
    def Start(self):
        self.btn.hide()
        self.btn2.hide()
        self.lbl2.show()
        for btn in self.lst_kataklar:
            btn.setEnabled(True)
            
    def Stop(self,user):
        self.btn3.show()
        self.btn2.show()
        self.lbl2.hide()
        
        for btn in self.lst_kataklar:
            btn.setEnabled(False)
            
        lst = self.lbl.text().split("|")
        son = lst[2].split("-")

        if user == lst[1].strip():
            yangi_hisob = f"Hisob: |{lst[1].strip()}| {int(son[0].strip()) + 1} - {son[1].strip()} |{lst[3].strip()}|"
            self.lbl.setText(yangi_hisob)
        elif user == lst[3].strip():
            yangi_hisob = f"Hisob: |{lst[1].strip()}| {son[0].strip()} - {int(son[1].strip()) + 1} |{lst[3].strip()}|"
            self.lbl.setText(yangi_hisob)
        elif user == 2:
            yangi_hisob = f"Hisob: |{lst[1].strip()}| {int(son[0].strip())+1} - {int(son[1].strip()) + 1} |{lst[3].strip()}|"
            self.lbl.setText(yangi_hisob)
            
            
                
    def Exit(self):
        self.hide()
        self.obj.show()
        
    def Davom_etish(self):
        for i in self.lst_kataklar:
            i.setText(" ")
            i.setEnabled(True)
            self.count = 0
        self.lbl2.show()
        self.btn2.hide()
        self.btn3.hide() 
    