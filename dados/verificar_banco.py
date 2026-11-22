import sqlite3

conexao = sqlite3.connect("dados/loki.db")

consulta = "SELECT name FROM sqlite_master WHERE type='table'"

tabelas = conexao.execute(consulta).fetchall()

for tabela in tabelas:
    print(tabela[0])

conexao.close()
