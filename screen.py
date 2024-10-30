from PyQt5.QtWidgets import *
from start_game import Start_game    
        
        
app = QApplication([])
win = Start_game()
win.show()
app.exec_()