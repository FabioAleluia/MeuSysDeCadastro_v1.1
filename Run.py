from PyQt5 import uic,QtWidgets
from Janelas import Janelas

def FazerLogin():
    welcome.close()
    tela_login.show()



app=QtWidgets.QApplication([])

# Janelas
win = Janelas.GetJanelas()
welcome = win.welcome
tela_login = win.win_login
tela_opcoes = win.win_opcoes

# Ações dos Botões
welcome.fazer_login.clicked.connect(FazerLogin)

welcome.show()
app.exec()