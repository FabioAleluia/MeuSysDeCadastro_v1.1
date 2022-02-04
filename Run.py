from signal import pause
from PyQt5 import uic,QtWidgets
from Janelas import Janelas
from Validacao import ValidarLogin
from Validacao import ValidarPfisica
from Validacao import ValidarPjuridica
from Banco_db import WriteDb

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

def CadastroPfisica():
    input_cpf = formulario_Pfisica.input_cpf.text()
    input_nome = formulario_Pfisica.input_nome.text()
    input_cep = formulario_Pfisica.input_cep.text()
    input_uf = formulario_Pfisica.input_uf.text()
    input_cidade = formulario_Pfisica.input_cidade.text()
    input_numero = formulario_Pfisica.input_numero.text()
    input_endereco = formulario_Pfisica.input_endereco.text()
    input_telefoneum = formulario_Pfisica.input_TelefoneUm.text()
    input_telefonedois = formulario_Pfisica.input_TelefoneDois.text()
    input_email = formulario_Pfisica.input_email.text()
    
    # Enviar os dados recebido do formulario, para serem validados
    send_db = ValidarPfisica.DadosPfisica(cpf=input_cpf, nome=input_nome, endereco=input_endereco, numero=input_numero, cep=input_cep, uf=input_uf, cidade=input_cidade, telefonefixo=input_telefoneum, telefonecelular=input_telefonedois, email=input_email)
    
    #---- Retorno da Validação (CPF) ----#
    cpf = send_db.cpf_invalido
    
    if cpf == 0:
        formulario_Pfisica.aviso_01.setText("*")
        print('CPF Invalido')
        return CadastroFisico()
        
    else:
        formulario_Pfisica.aviso_01.setText("")
        print('CPF Valido')
    
    #---- Retorno da Validação (Nome) ----#
    nome = send_db.nome_valido
    
    if nome == 0:
        formulario_Pfisica.aviso_02.setText("*")
        print('Nome INVALIDO')
        return CadastroFisico()
    
    else:
        pass
        formulario_Pfisica.aviso_02.setText("")
        print('Nome VALIDO')
    
    send_db = WriteDb.Pfisica(cpf=input_cpf, nome=send_db.input_nome, endereco='input_endereco', numero='input_numero', cep='input_cep', uf='input_uf', cidade='input_cidade', telefonefixo='input_TelefoneFixo', telefonecelular='input_TelefoneCelular', email='input_email')

def CadastroPjuridica():
    input_cnpj = formulario_Pjuridica.input_cpf.text()
    input_razaosocial = formulario_Pjuridica.input_razaosocial.text()
    input_cep = formulario_Pjuridica.input_cep.text()
    input_uf = formulario_Pjuridica.input_uf.text()
    input_cidade = formulario_Pjuridica.input_cidade.text()
    input_endereco = formulario_Pjuridica.input_endereco.text()
    input_numero = formulario_Pjuridica.input_numero.text()
    input_telefoneum = formulario_Pjuridica.input_TelefoneUm.text()
    input_telefonedois = formulario_Pjuridica.input_TelefoneDois.text()
    input_email = formulario_Pjuridica.input_email.text()
    
    send_db = ValidarPjuridica.DadosPjuridica(cnpj=input_cnpj, nome=input_razaosocial, endereco=input_endereco, numero=input_numero, cep=input_cep, uf=input_uf, cidade=input_cidade, telefonefixo=input_telefoneum, telefonecelular=input_telefonedois, email=input_email)
    
    cnpj = send_db.cnpj_invalido
    
    if cnpj == 0:
        print('CNPJ Invalido')
    
    else:
        pass
        print('CNPJ Valido')
    
    write_db = WriteDb.Pjuridica(cnpj=send_db.cnpj_valido, razaos=input_razaosocial, endereco=input_endereco, numero=input_numero, cep=input_cep, uf=input_uf, cidade=input_cidade, telefonefixo=input_telefoneum, telefonecelular=input_telefonedois, email=input_email)
    
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

def Teste():
    print('Teste de Click')

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
formulario_Pfisica.salva_dados.clicked.connect(CadastroPfisica)
formulario_Pjuridica.salva_dados.clicked.connect(CadastroPjuridica)

tela_login.senha.setEchoMode(QtWidgets.QLineEdit.Password)
criar_login.senha.setEchoMode(QtWidgets.QLineEdit.Password)


## Tamanho das Janelas
welcome.setFixedSize(461,426)
tela_login.setFixedSize(461,426)
criar_login.setFixedSize(461,426)
tela_opcoes.setFixedSize(601,500)

welcome.show()
app.exec()
