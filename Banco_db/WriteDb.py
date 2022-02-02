from dataclasses import dataclass
import sqlite3
import time


class Pfisica:
    def __init__(self, cpf, nome, endereco, numero, cep, uf, cidade, telefonefixo, telefonecelular, email, dt, ha):
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
        self.dt = dt
        self.ha = ha
    
        # Local onde esta o arquivo do Banco de Dados.
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.1_qt/Banco_db/Banco_dd.db"
    
        conexao_db = sqlite3.connect(dir_db) # Realizar conexão do arquivo do Banco de Dados
        cursor = conexao_db.cursor()
        d = '12:00'

        cursor.execute("INSERT INTO pessoafisica VALUES ('"+self.cpf+"', '"+self.nome+"', '"+self.endereco+"', '"+self.numero+"', '"+self.cep+"', '"+self.uf+"', '"+self.cidade+"', '"+self.telefonefixo+"', '"+self.telefonecelular+"', '"+self.email+"', '"+self.dt+"', '"+self.ha+"')")

        conexao_db.commit()
        conexao_db.close()

class Pjuridica:
    def __init__(self, cnpj, nome, endereco, numero, cep, uf, cidade, telefonefixo, telefonecelular, email, dt, ha):
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
        self.dt = dt
        self.ha = ha
    
        # Local onde esta o arquivo do Banco de Dados.
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.1_qt/Banco_db/Banco_dd.db"
    
        conexao_db = sqlite3.connect(dir_db) # Realizar conexão do arquivo do Banco de Dados
        cursor = conexao_db.cursor()
        d = '12:00'

        cursor.execute("INSERT INTO pessojuridica VALUES ('"+self.cpf+"', '"+self.nome+"', '"+self.endereco+"', '"+self.numero+"', '"+self.cep+"', '"+self.uf+"', '"+self.cidade+"', '"+self.telefonefixo+"', '"+self.telefonecelular+"', '"+self.email+"', '"+self.dt+"', '"+self.ha+"')")

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
