from PyQt5 import uic,QtWidgets

class GetJanelas:
    def __init__(self):
        self.welcome = welcome=uic.loadUi("Janelas/Windows/welcome.ui")
        self.win_login = login=uic.loadUi("Janelas/Windows/login_win_one.ui")
        self.win_opcoes = opcoes=uic.loadUi("Janelas/Windows/opcoes_win_one.ui")
        self.win_criar_login = criar_login=uic.loadUi("Janelas/Windows/criar_login.ui") 
        self.win_formulario_Pfisica = formulario_Pfisica=uic.loadUi("Janelas/Windows/formulario_P_fisica.ui")
        self.win_formulario_Pjuridica = formulario_Pjuridica=uic.loadUi("Janelas/Windows/formulario_P_juridica.ui")
        