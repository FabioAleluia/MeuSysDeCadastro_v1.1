from dataclasses import dataclass
import sqlite3
import time


class Pfisica:
    def __init__(self, cpf, nome, cep, uf, cidade, endereco, numero, telefonefixo, telefonecelular, email):
        self.cpf = cpf
        self.nome = nome
        self.cep = cep
        self.uf = uf
        self.cidade = cidade
        self.endereco = endereco
        self.numero = numero
        self.telefonefixo = telefonefixo
        self.telefonecelular = telefonecelular
        self.email = email

        dta = time.strftime('%d/%m/%y')
        hra = time.strftime('%H:%M:%S')

        # Local onde esta o arquivo do Banco de Dados.
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.1_qt/Banco_db/Banco_dd.db"
    
        conexao_db = sqlite3.connect(dir_db) # Realizar conexão do arquivo do Banco de Dados
        cursor = conexao_db.cursor()

        cursor.execute("INSERT INTO pessoafisica VALUES ('"+self.cpf+"', '"+self.nome+"', '"+self.cep+"', '"+self.uf+"', '"+self.cidade+"', '"+self.endereco+"', '"+self.numero+"', '"+self.telefonefixo+"', '"+self.telefonecelular+"', '"+self.email+"', '"+dta+"', '"+hra+"')")

        conexao_db.commit()
        conexao_db.close()

class Pjuridica:
    def __init__(self, cnpj, razaos, endereco, numero, cep, uf, cidade, telefonefixo, telefonecelular, email):
        self.cnpj = cnpj
        self.razaos = razaos
        self.endereco = endereco
        self.numero = numero
        self.cep = cep
        self.uf = uf
        self.cidade = cidade
        self.telefonefixo = telefonefixo
        self.telefonecelular = telefonecelular
        self.email = email

        dta = time.strftime('%d/%m/%y')
        hra = time.strftime('%H:%M:%S')
            
        # Local onde esta o arquivo do Banco de Dados.
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.1_qt/Banco_db/Banco_dd.db"
    
        conexao_db = sqlite3.connect(dir_db) # Realizar conexão do arquivo do Banco de Dados
        cursor = conexao_db.cursor()

        cursor.execute("INSERT INTO pessoajuridica VALUES ('"+self.cnpj+"', '"+self.razaos+"', '"+self.endereco+"', '"+self.numero+"', '"+self.cep+"', '"+self.uf+"', '"+self.cidade+"', '"+self.telefonefixo+"', '"+self.telefonecelular+"', '"+self.email+"', '"+dta+"', '"+hra+"')")

        conexao_db.commit()
        conexao_db.close()

class NovoUser:
    
    def __init__(self, usuario, senha, dt, ha):
        self.usuario = usuario
        self.senha = senha
        self.dt = dt
        self.ha = ha
      
        # Local onde esta o arquivo do Banco de Dados.
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.1_qt/Banco_db/Banco_dd.db"

        conexao_db = sqlite3.connect(dir_db) # Realizar conexão do arquivo do Banco de Dados
        cursor = conexao_db.cursor()
        d = '12:00'

        cursor.execute("INSERT INTO validalogin VALUES ('"+self.usuario+"', '"+self.senha+"', '"+self.dt+"', '"+self.ha+"')")

        conexao_db.commit()
        conexao_db.close()
