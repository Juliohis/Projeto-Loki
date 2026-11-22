
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    ano INTEGER,
    era TEXT,
    publicadora TEXT,
    serie TEXT,
    genero TEXT,
    estilo_de_jogo TEXT,
    visao TEXT,
    jogadores_max INTEGER,
    multiplayer TEXT,
    modo_multiplayer TEXT,
    cooperativo TEXT,
    ambientacao TEXT,
    protagonista TEXT,
    estilo_visual TEXT,
    clima TEXT,
    trilha_sonora TEXT,
    ritmo TEXT,
    dificuldade TEXT,
    duracao TEXT,
    salva_progresso_tipo TEXT,
    salva_progresso TEXT,
    usa_mode7 TEXT,
    idioma TEXT,
    lancado_na_america_do_norte TEXT,
    so_no_japao TEXT,
    publicado_pela_nintendo TEXT,
    descricao TEXT,
    capa TEXT
);

CREATE TABLE IF NOT EXISTS desenvolvedoras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS tecnologias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS regioes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS compositores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS jogos_desenvolvedoras (
    jogo_id INTEGER,
    desenvolvedora_id INTEGER,
    PRIMARY KEY (jogo_id, desenvolvedora_id),
    FOREIGN KEY (jogo_id) REFERENCES jogos(id),
    FOREIGN KEY (desenvolvedora_id) REFERENCES desenvolvedoras(id)
);

CREATE TABLE IF NOT EXISTS jogos_tecnologias (
    jogo_id INTEGER,
    tecnologia_id INTEGER,
    PRIMARY KEY (jogo_id, tecnologia_id),
    FOREIGN KEY (jogo_id) REFERENCES jogos(id),
    FOREIGN KEY (tecnologia_id) REFERENCES tecnologias(id)
);

CREATE TABLE IF NOT EXISTS jogos_regioes (
    jogo_id INTEGER,
    regiao_id INTEGER,
    PRIMARY KEY (jogo_id, regiao_id),
    FOREIGN KEY (jogo_id) REFERENCES jogos(id),
    FOREIGN KEY (regiao_id) REFERENCES regioes(id)
);

CREATE TABLE IF NOT EXISTS jogos_personagens (
    jogo_id INTEGER,
    personagem_id INTEGER,
    PRIMARY KEY (jogo_id, personagem_id),
    FOREIGN KEY (jogo_id) REFERENCES jogos(id),
    FOREIGN KEY (personagem_id) REFERENCES personagens(id)
);

CREATE TABLE IF NOT EXISTS jogos_compositores (
    jogo_id INTEGER,
    compositor_id INTEGER,
    PRIMARY KEY (jogo_id, compositor_id),
    FOREIGN KEY (jogo_id) REFERENCES jogos(id),
    FOREIGN KEY (compositor_id) REFERENCES compositores(id)
);
