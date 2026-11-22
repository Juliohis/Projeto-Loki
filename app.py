
import sqlite3
from pathlib import Path
from flask import Flask, jsonify, request

app = Flask(__name__)

# Localiza o banco de dados
BASE_DIR = Path(__file__).resolve().parent
CAMINHO_BANCO = BASE_DIR / "dados" / "loki.db"


def conectar_banco():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


@app.route("/api/jogos", methods=["GET"])
def listar_jogos():
    conexao = conectar_banco()

    jogos = conexao.execute(
        "SELECT id, nome, ano, genero, descricao, capa FROM jogos"
    ).fetchall()

    conexao.close()

    resultado = [dict(jogo) for jogo in jogos]

    return jsonify(resultado)

@app.route("/api/buscar", methods=["POST"])
def buscar_jogos():
    filtros = request.get_json()
    condicoes = []
    valores = []   
    campos_permitidos = {   
        "genero": "genero",
        "estilo_de_jogo": "estilo_de_jogo",
        "visao": "visao"
}
    for chave, coluna in campos_permitidos.items():
        selecionados = filtros.get(chave, [])
        
        if selecionados:
            placeholders = ", ".join(["?"] * len(selecionados))
            condicoes.append(f"{coluna} IN ({placeholders})")
            valores.extend(selecionados)
        
    sql = "SELECT id, nome, ano, genero, descricao, capa FROM jogos"
    
    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)
       
    conexao = conectar_banco()

    jogos = conexao.execute(sql, valores).fetchall()

    conexao.close()
        
    resultado = [dict(jogo) for jogo in jogos]

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)
