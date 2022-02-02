#from Validacao import Gateway

class ValidiLogin:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
        if not self.usuario:
            print('nada')    
        
        else:
            self.allon = 'Acesso ok'