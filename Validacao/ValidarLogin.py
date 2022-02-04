#from Validacao import Gateway
import hashlib
import sqlite3
import mysql.connector

class ValidiLogin:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

        join_us = (self.usuario) + (self.senha)
        hash_criado = hashlib.sha256(join_us.encode('utf-8')).hexdigest()
        
        con = mysql.connector.connect(host='192.168.0.104',database='Banco_dd',user='admin',password='1992')
        cursor = con.cursor()
        
        cursor.execute("select database();")
        cursor.execute("SELECT senha FROM UserPass")

        result_tabela = str(cursor.fetchone())
        
        if hash_criado in self.result_tabela:
            self.liberado = int(1)

        else:
            self.liberado = 0

'''
class ValidiLogin:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
        join_us = (self.usuario) + (self.senha)
        hash_criado = hashlib.sha256(join_us.encode('utf-8')).hexdigest()
        
        dir_db = "Banco_db/Banco_dd.db"
        conexao = sqlite3.connect(dir_db)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT senha FROM userpass")
        self.result_tabela = str(cursor.fetchall())
        
        if hash_criado in self.result_tabela:
            self.liberado = int(1)

        else:
            self.liberado = 0
'''
        
        