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

        dt = time.strftime('%d/%m/%y')
        ha = time.strftime('%H:%M:%S')
        
        valida_cpf = self.cpf.strip()
        valida_cpf = valida_cpf.replace(" ","")
        
        if valida_cpf.isnumeric():
            valida_cpf = len(valida_cpf)
            valida_cpf = int(valida_cpf)
                
            if valida_cpf < 11 or valida_cpf > 11:
                #self.aviso_01 = "*"
                erro_input_cpf = 0

            if valida_cpf == 11:
                input_cpf = str(self.cpf.strip())
                input_cpf = str(input_cpf.replace(" ",""))
                self.input_cpf = input_cpf
                #tela_formulario.aviso_01.setText("")
                #tela_formulario.a_input_cpf.setText(input_cpf)
                erro_input_cpf = 1
                print(input_cpf)
            
            else:
                input_cpf = str(valida_cpf)
                
        else:
            #self.aviso_01 = "*"
            erro_input_cpf = 0
        
        send_db = WriteDb.Pfisica(cpf=input_cpf, nome='input_nome', endereco='input_endereco', numero='input_numero', cep='input_cep', uf='input_uf', cidade='input_cidade', telefonefixo='input_TelefoneFixo', telefonecelular='input_TelefoneCelular', email='input_email', dt=dt, ha=ha)