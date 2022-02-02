#from Validacao import Gateway
import hashlib
import sqlite3

class ValidiLogin:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
        join_us = (self.usuario) + (self.senha)
        hash_criado = hashlib.sha256(join_us.encode('utf-8')).hexdigest()
        
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.1_qt/Banco_db/Banco_dd.db"
        conexao = sqlite3.connect(dir_db)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT senha FROM userpass")
        self.result_tabela = str(cursor.fetchall())
        
        if hash_criado in self.result_tabela:
            self.liberado = int(1)

        else:
            self.liberado = 0

        
        