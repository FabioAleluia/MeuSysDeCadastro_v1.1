import mysql.connector

con = mysql.connector.connect(host='192.168.0.104',database='Banco_dd',user='admin',password='1992')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    #cursor.execute("select database();")
    
    usuario_senha = ("Fabio", "123")
    
    comando_SQL = ("INSERT INTO UserPass (usuario, senha) VALUES (%s, %s)")
    
    cursor.execute(comando_SQL, usuario_senha)
    
    cursor.execute("SELECT senha FROM UserPass")
    
    linha = cursor.fetchone()
    
    print("Conectado ao banco de dados ",linha)
    
    #con.commit()


if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")