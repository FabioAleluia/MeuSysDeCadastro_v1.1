import sqlite3
import time
from Banco_db import WriteDb

class DadosPjuridica:
    def __init__(self, cnpj, nome, endereco, numero, cep, uf, cidade, telefonefixo, telefonecelular, email):
        self.cnpj = cnpj
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.cep = cep
        self.uf = uf
        self.cidade = cidade
        self.telefonefixo = telefonefixo
        self.telefonecelular = telefonecelular
        self.email = email
        
        valida_cnpj = self.cnpj.strip()
        valida_cnpj = valida_cnpj.replace(" ","")
        
        if valida_cnpj.isnumeric():
            valida_cnpj = len(valida_cnpj)
            valida_cnpj = int(valida_cnpj)
            
            if valida_cnpj < 14 or valida_cnpj > 14:
                cnpj_invalido = 0
            
            if valida_cnpj == 14:
                input_cnpj = str(self.cnpj.strip())
                input_cnpj = input_cnpj.replace(" ","")
                self.cnpj_invalido = 1
                self.cnpj_valido = input_cnpj
                #print(input_razaosocial)
            
            else:
                self.cnpj_invalido = 0
        
        else:
            self.cnpj_invalido = 0