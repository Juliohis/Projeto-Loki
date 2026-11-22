
import json
import sqlite3
from pathlib import Path

# Localiza a pasta onde este arquivo está
BASE_DIR = Path(__file__).resolve().parent

# Define os caminhos dos arquivos
CAMINHO_JSON = BASE_DIR / "snes_jogos_com_capas.json"
CAMINHO_BANCO = BASE_DIR / "loki.db"


def normalizar_lista(valor):
    """Transforma valores separados por vírgula em uma lista."""
    if not valor:
        return []

    if valor.strip().lower() in ("-", "nenhuma"):
        return []

    return [
        item.strip()
        for item in valor.split(",")
        if item.strip() and item.strip() != "-"
    ]


def obter_id_catalogo(cursor, tabela, nome):
    """Busca um item no catálogo ou cadastra se ele ainda não existir."""
    cursor.execute(
        f"INSERT OR IGNORE INTO {tabela} (nome) VALUES (?)",
        (nome,)
    )

    cursor.execute(
        f"SELECT id FROM {tabela} WHERE nome = ?",
        (nome,)
    )

    return cursor.fetchone()[0]


# Carrega os dados do JSON
with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
    registros = json.load(arquivo)


# Define as relações entre os campos do JSON e as tabelas SQL
relacoes = {
    "desenvolvedora": ("desenvolvedoras", "jogos_desenvolvedoras", "desenvolvedora_id"),
    "tecnologia_especial": ("tecnologias", "jogos_tecnologias", "tecnologia_id"),
    "regioes": ("regioes", "jogos_regioes", "regiao_id"),
    "personagens": ("personagens", "jogos_personagens", "personagem_id"),
    "compositores": ("compositores", "jogos_compositores", "compositor_id")
}


# Conecta ao banco e inicia a importação
with sqlite3.connect(CAMINHO_BANCO) as conexao:
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

    for jogo in registros:

        # Dados que serão inseridos na tabela principal
        valores = (
            jogo["jogo"],
            jogo["ano"],
            jogo["era"],
            jogo["publicadora"],
            jogo["serie"],
            jogo["genero"],
            jogo["estilo_de_jogo"],
            jogo["visao"],
            jogo["jogadores_max"],
            jogo["multiplayer"],
            jogo["modo_multiplayer"],
            jogo["cooperativo"],
            jogo["ambientacao"],
            jogo["protagonista"],
            jogo["estilo_visual"],
            jogo["clima"],
            jogo["trilha_sonora"],
            jogo["ritmo"],
            jogo["dificuldade"],
            jogo["duracao"],
            jogo["salva_progresso_tipo"],
            jogo["salva_progresso"],
            jogo["usa_mode7"],
            jogo["idioma"],
            jogo["lancado_na_america_do_norte"],
            jogo["so_no_japao"],
            jogo["publicado_pela_nintendo"],
            jogo["descricao"],
            jogo["capa"]
        )

        colunas = """
            nome, ano, era, publicadora, serie, genero,
            estilo_de_jogo, visao, jogadores_max, multiplayer,
            modo_multiplayer, cooperativo, ambientacao, protagonista,
            estilo_visual, clima, trilha_sonora, ritmo, dificuldade,
            duracao, salva_progresso_tipo, salva_progresso, usa_mode7,
            idioma, lancado_na_america_do_norte, so_no_japao,
            publicado_pela_nintendo, descricao, capa
        """

        marcadores = ", ".join(["?"] * len(valores))

        cursor.execute(
            f"INSERT OR IGNORE INTO jogos ({colunas}) VALUES ({marcadores})",
            valores
        )

        # Recupera o ID do jogo cadastrado
        cursor.execute(
            "SELECT id FROM jogos WHERE nome = ?",
            (jogo["jogo"],)
        )

        jogo_id = cursor.fetchone()[0]

        # Cadastra os dados das tabelas relacionadas
        for campo, (tabela, tabela_relacao, coluna_id) in relacoes.items():

            itens = normalizar_lista(jogo.get(campo, ""))

            for item in itens:
                item_id = obter_id_catalogo(cursor, tabela, item)

                cursor.execute(
                    f"""
                    INSERT OR IGNORE INTO {tabela_relacao}
                    (jogo_id, {coluna_id})
                    VALUES (?, ?)
                    """,
                    (jogo_id, item_id)
                )


# Confere quantos jogos foram importados
with sqlite3.connect(CAMINHO_BANCO) as conexao:
    total = conexao.execute(
        "SELECT COUNT(*) FROM jogos"
    ).fetchone()[0]

print(f"Importação concluída! Total de jogos no banco: {total}")
