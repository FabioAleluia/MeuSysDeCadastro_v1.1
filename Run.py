from PyQt5 import uic,QtWidgets
from Janelas import Janelas

def FazerLogin():
    welcome.close()
    tela_login.show()

def VoltaWelcome():
    tela_login.close()
    welcome.show()

def CriarLogin(): # Volta da tela de "Login" para tela de Bem-Vindo
    welcome.close()
    criar_login.show()

def clforwelcome(): # Volta da Tela "Criar Login" para tela de Bem-Vindo
    criar_login.close()
    welcome.show()

app=QtWidgets.QApplication([])

# Janelas
win = Janelas.GetJanelas()

welcome = win.welcome
tela_login = win.win_login
criar_login = win.win_criar_login
tela_opcoes = win.win_opcoes


# Ações dos Botões
welcome.fazer_login.clicked.connect(FazerLogin)
welcome.criar_login.clicked.connect(CriarLogin)
tela_login.volta.clicked.connect(VoltaWelcome)
criar_login.volta.clicked.connect(clforwelcome)

welcome.show()
app.exec()