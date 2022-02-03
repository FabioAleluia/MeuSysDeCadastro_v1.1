import sqlite3
import time
from Banco_db import WriteDb

class DadosPfisica:
    def __init__(self, cpf, nome, endereco, numero, cep, uf, cidade, telefonefixo, telefonecelular, email):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.cep = cep
        self.uf = uf
        self.cidade = cidade
        self.telefonefixo = telefonefixo
        self.telefonecelular = telefonecelular
        self.email = email
        
        valida_cpf = self.cpf.strip()
        valida_cpf = valida_cpf.replace(" ","")
        
        if valida_cpf.isnumeric():
            valida_cpf = len(valida_cpf)
            valida_cpf = int(valida_cpf)
                
            if valida_cpf < 11 or valida_cpf > 11:
                cpf_invalido = 0

            if valida_cpf == 11:
                input_cpf = str(self.cpf.strip())
                input_cpf = str(input_cpf.replace(" ",""))
                self.cpf_invalido = 1
                print(input_cpf)
            
            else:
                self.cpf_invalido = 0
                
        else:
            self.cpf_invalido = 0
        