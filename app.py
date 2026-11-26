import os
import sqlite3
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

FRONTEND_URL = os.environ.get("FRONTEND_URL")

if FRONTEND_URL:
    CORS(app, origins=[FRONTEND_URL])
else:
    CORS(app)


# Localiza o banco de dados
BASE_DIR = Path(__file__).resolve().parent
CAMINHO_BANCO = BASE_DIR / "dados" / "loki.db"
CAMINHO_CAPAS = BASE_DIR / "dados" / "capas"

def conectar_banco():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route("/capas/<nome_arquivo>")
def servir_capa(nome_arquivo):
    return send_from_directory(CAMINHO_CAPAS, nome_arquivo)

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

@app.route("/api/opcoes", methods=["GET"])
def listar_opcoes():
    conexao = conectar_banco()

    generos = conexao.execute(
        "SELECT DISTINCT genero FROM jogos WHERE genero IS NOT NULL ORDER BY genero"
    ).fetchall()

    estilos = conexao.execute(
        "SELECT DISTINCT estilo_de_jogo FROM jogos WHERE estilo_de_jogo IS NOT NULL ORDER BY estilo_de_jogo"
    ).fetchall()

    visoes = conexao.execute(
        "SELECT DISTINCT visao FROM jogos WHERE visao IS NOT NULL ORDER BY visao"
    ).fetchall()

    conexao.close()

    return jsonify({
        "generos": [linha[0] for linha in generos],
        "estilos": [linha[0] for linha in estilos],
        "visoes": [linha[0] for linha in visoes]
    })
@app.route("/api/estilos", methods=["GET"])
def listar_estilos():
    genero = request.args.getlist("genero")
    visao = request.args.getlist("visao")

    condicoes = []
    valores = []

    if genero:
        placeholders = ", ".join(["?"] * len(genero))
        condicoes.append(f"genero IN ({placeholders})")
        valores.extend(genero)

    if visao:
        placeholders = ", ".join(["?"] * len(visao))
        condicoes.append(f"visao IN ({placeholders})")
        valores.extend(visao)

    sql = """
        SELECT DISTINCT estilo_de_jogo
        FROM jogos
        WHERE estilo_de_jogo IS NOT NULL
    """

    if condicoes:
        sql += " AND " + " AND ".join(condicoes)

    sql += " ORDER BY estilo_de_jogo"

    conexao = conectar_banco()
    estilos = conexao.execute(sql, valores).fetchall()
    conexao.close()

    return jsonify([linha[0] for linha in estilos])

if __name__ == "__main__":
    app.run(debug=True)
