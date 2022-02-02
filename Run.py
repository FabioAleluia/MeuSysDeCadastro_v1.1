from PyQt5 import uic,QtWidgets
from Janelas import Janelas
from Validacao import ValidarLogin


def InputLogin():
    tela_login.aviso_login.clear()
    inputuser = tela_login.usuario.text()
    inputsenha = tela_login.senha.text()
    sendvalidlogin = ValidarLogin.ValidiLogin(usuario=inputuser, senha=inputsenha)
    
    result_consul = sendvalidlogin.liberado
    allow = 1
    
    if allow == result_consul:
        MenuOpcoes()
    
    else:
        tela_login.aviso_login.setText("Usuário ou senha incorreto.")
        

def FazerLogin(): # Sai da Tela de "Bem-Vindo" e vai para a Tela de "Login"
    tela_login.aviso_login.clear()
    tela_login.usuario.clear()
    tela_login.senha.clear()
    welcome.close()
    tela_login.show()

def VoltaWelcome(): # Sai da Tela de "Login" e volta pra Tela de "Bem-Vindo"
    tela_login.close()
    welcome.show()

def CriarLogin(): # Sai da Tela "Bem-Vindo" e vai pra tela de "Criar Login"
    welcome.close()
    criar_login.show()

def clforwelcome(): # Sai da Tela de "Criar Login" e volta pra tela de "Bem-Vindo"
    criar_login.close()
    welcome.show()

def MenuOpcoes():
    tela_login.close()
    tela_opcoes.show()

def OpcoesForLogin():
    tela_login.usuario.clear()
    tela_login.senha.clear()
    tela_opcoes.close()
    tela_login.show()

def CadastroFisico():
    tela_opcoes.close()
    formulario_Pfisica.show()

def CadastroJuridico():
    tela_opcoes.close()
    formulario_Pjuridica.show()

def VoltaParaOpcoes_1():
    formulario_Pjuridica.close()
    tela_opcoes.show()

def VoltaParaOpcoes_2():
    formulario_Pfisica.close()
    tela_opcoes.show()

class Catalago:
    def Teste():
        print('OI')

app=QtWidgets.QApplication([])

# Janelas
win = Janelas.GetJanelas()

welcome = win.welcome
tela_login = win.win_login
criar_login = win.win_criar_login
tela_opcoes = win.win_opcoes
formulario_Pfisica = win.win_formulario_Pfisica
formulario_Pjuridica = win.win_formulario_Pjuridica

# Ações dos Botões
welcome.fazer_login.clicked.connect(FazerLogin)
welcome.criar_login.clicked.connect(CriarLogin)
tela_login.login.clicked.connect(InputLogin)
tela_login.volta.clicked.connect(VoltaWelcome)
criar_login.volta.clicked.connect(clforwelcome)
tela_opcoes.logoff.clicked.connect(OpcoesForLogin)
tela_opcoes.p_juridica.clicked.connect(CadastroJuridico)
tela_opcoes.p_fisica.clicked.connect(CadastroFisico)
formulario_Pjuridica.volta.clicked.connect(VoltaParaOpcoes_1)
formulario_Pfisica.volta.clicked.connect(VoltaParaOpcoes_2)

tela_login.senha.setEchoMode(QtWidgets.QLineEdit.Password)
criar_login.senha.setEchoMode(QtWidgets.QLineEdit.Password)


## Tamanho das Janelas
welcome.setFixedSize(461,426)
tela_login.setFixedSize(461,426)
criar_login.setFixedSize(461,426)
tela_opcoes.setFixedSize(601,500)

welcome.show()
app.exec()
