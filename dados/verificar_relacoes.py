
import sqlite3

conexao = sqlite3.connect("dados/loki.db")

tabelas = [
    "jogos",
    "desenvolvedoras",
    "tecnologias",
    "regioes",
    "personagens",
    "compositores",
    "jogos_desenvolvedoras",
    "jogos_tecnologias",
    "jogos_regioes",
    "jogos_personagens",
    "jogos_compositores"
]

print("RESUMO DO BANCO DE DADOS\n")

for tabela in tabelas:
    consulta = f"SELECT COUNT(*) FROM {tabela}"
    total = conexao.execute(consulta).fetchone()[0]

    print(f"{tabela}: {total} registros")


print("\nVERIFICAÇÃO DE INTEGRIDADE")

erros = conexao.execute("PRAGMA foreign_key_check").fetchall()

if erros:
    print("Foram encontrados problemas:", erros)
else:
    print("Nenhum problema de chave estrangeira encontrado.")


conexao.close()

