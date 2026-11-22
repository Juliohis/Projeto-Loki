import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

CAMINHO_BANCO = BASE_DIR / "loki.db"
CAMINHO_SCHEMA = BASE_DIR / "schema.sql"


conexao = sqlite3.connect(CAMINHO_BANCO)

with open(CAMINHO_SCHEMA, "r", encoding="utf-8") as arquivo:
    sql = arquivo.read()
    conexao.executescript(sql)
    
conexao.close()

print("Banco de dados criado com sucesso!")
