import sqlite3
import time
from Banco_db import WriteDb

class DadosPfisica:
    def __init__(self, cpf, nome, cep, uf, cidade, endereco, numero, telefonefixo, telefonecelular, email):
        self.cpf = cpf
        self.nome = nome
        self.cep = cep
        self.uf = uf
        self.cidade = cidade
        self.endereco = endereco
        self.cidade = numero
        self.telefonefixo = telefonefixo
        self.telefonecelular = telefonecelular
        self.email = email
        
        # Validação do (CPF)
        valida_cpf = self.cpf.strip()
        valida_cpf = valida_cpf.replace(" ","")
        
        if valida_cpf.isnumeric():
            valida_cpf = len(valida_cpf)
            valida_cpf = int(valida_cpf)
                
            if valida_cpf < 11 or valida_cpf > 11:
                cpf_invalido = 0
                   
                
            if valida_cpf == 11:
                input_cpf = str(self.cpf.strip())
                self.input_cpf = str(input_cpf.replace(" ",""))
                self.cpf_invalido = 1
                self.cpf_ok = self.input_cpf
            
            else:
                self.cpf_invalido = 0
                
        else:
            self.cpf_invalido = 0
        
        # Validação do (Nome)
        valida_nome = self.nome.strip()
        valida_nome = valida_nome.replace(" ","")
        
        if valida_nome.isalpha():
            valida_nome = len(valida_nome)
            valida_nome = int(valida_nome)
            
            if valida_nome < 5 or valida_nome > 45:
                self.nome_valido = 0
            
            if valida_nome >= 5 or valida_nome <= 45:
                self.input_nome = str(self.nome.strip())
                self.nome_valido = 1
                self.nome_ok = self.input_nome
                
            else:
                self.nome_valido = 0
        
        else:
            self.nome_valido = 0
        
        # Validação (CEP)
        valida_cep = self.cep.strip()
        valida_cep = valida_cep.replace(" ","")
        
        if valida_cep.isnumeric():
            valida_cep = len(valida_cep)
            valida_cep = int(valida_cep)
            
            if valida_cep < 8 or valida_cep > 8:
                self.cep_valido = 0
                self.input_cep = 'CEP'
            
            if valida_cep == 8:
                self.input_cep = str(valida_cep)
                self.cep_valido = 1
                self.cep_ok = self.input_cep
                    
            else:
                self.cep_valido = 0
        
        else:
            self.cep_valido = 0
        
        