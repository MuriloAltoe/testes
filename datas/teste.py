from datetime import date, datetime
from distutils.util import execute
import sqlite3
from webbrowser import get
import datetime

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

esc = input("Escolha oque ira fazer \n1- Adicionar \n2- Atualizar \n3- Deletar\n Ou qualquer coisa para sair\n ")

if esc == 1:
    data_entrada = datetime.datetime.now()
    codigo = input("Codigo: ")
    data_saida = datetime.datetime.now()
    cursor.execute("INSERT INTO registro (codigo, data_entrada, data_saida) VALUES (?, ?, ?)", (codigo, data_entrada, data_saida))
    conn.commit()
    cursor.execute("SELECT * FROM REGISTRO ORDER BY codigo")
    print(cursor.fetchall())

elif esc == 2:
    data_entrada = datetime.datetime.now()
    codigo = input("Codigo: ")
    data_saida = datetime.datetime.now()
    cursor.execute("UPDATE registro SET data_entrada=?, data_saida=? WHERE codigo=?", (data_entrada, data_entrada, codigo))
    conn.commit()
    print("Atualizado")
    cursor.execute("SELECT * FROM REGISTRO ORDER BY codigo")
    print(cursor.fetchall())

elif esc == 3:
    codigo = input("Codigo: ")
    cursor.execute("DELETE FROM registro WHERE codigo=?", (codigo))
    conn.commit()
    print("Deletado")
    cursor.execute("SELECT * FROM REGISTRO ORDER BY codigo")
    print(cursor.fetchall())
    
else:
    quit()

conn.close()
quit()
