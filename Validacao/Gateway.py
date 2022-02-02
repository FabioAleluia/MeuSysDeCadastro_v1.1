#from Run import Catalago
#from Validacao import ValidarLogin

class Conexao:
    def __init__(self, ok):
        self.ok = ok
        
        print(f'{self.ok} chegou no Gateway')