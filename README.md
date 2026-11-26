# Projeto Loki 🎮

**Sistema web de identificação e consulta de jogos do Super Nintendo (SNES).**

O Projeto Loki é uma aplicação desenvolvida para ajudar usuários a identificar jogos clássicos do Super Nintendo Entertainment System por meio da seleção de características visuais e de jogabilidade.

O sistema utiliza filtros e consultas a um banco de dados relacional para encontrar jogos compatíveis com as características selecionadas.

**Desenvolvedor:** Júlio de Almeida Prazeres

## 🌐 Acesso à aplicação

- **Aplicação:** https://projeto-loki-site.onrender.com
- **API:** https://projeto-loki.onrender.com

> A hospedagem utiliza o plano gratuito da Render. O backend pode levar alguns segundos para responder após um período de inatividade.

## ✨ Funcionalidades

- Identificação de jogos por características.
- Catálogo de jogos cadastrados.
- Consulta de informações e capas.
- Navegação por páginas com Vue Router.
- Comunicação entre frontend e backend por API REST.

## 🛠️ Tecnologias utilizadas

### Frontend
- Vue.js
- JavaScript
- Vite
- Vue Router
- HTML e CSS

### Backend
- Python
- Flask
- Flask-CORS
- Gunicorn

### Banco de dados
- SQLite

### Hospedagem
- Render (Static Site e Web Service)
- Git e GitHub para versionamento.

## 🧠 Como funciona a identificação?

O usuário seleciona características disponíveis no sistema. O frontend envia essas escolhas para a API, que realiza consultas ao banco de dados.

A lógica de filtragem funciona da seguinte maneira:

- **Dentro da mesma categoria:** as opções selecionadas são combinadas com OR.
- **Entre categorias diferentes:** os filtros são combinados com AND.
- **Categorias sem seleção:** não restringem os resultados.

Assim, o conjunto de jogos candidatos diminui conforme as características são selecionadas.

A primeira versão utiliza regras de filtragem e consultas ao banco de dados, sem modelos de Inteligência Artificial ou Machine Learning.

## 🗄️ Banco de dados

O projeto utiliza SQLite e possui uma base com 272 jogos cadastrados.

Entre as entidades armazenadas estão:

- Jogos;
- Desenvolvedoras;
- Tecnologias;
- Regiões;
- Personagens;
- Compositores.

O relacionamento entre jogos e as demais entidades é organizado por tabelas intermediárias quando necessário.

## 🔌 API

Principais rotas disponíveis:

| Rota | Função |
|---|---|
| `/api/jogos` | Lista os jogos cadastrados |
| `/api/buscar` | Busca jogos pelas características informadas |
| `/api/opcoes` | Retorna opções de características |
| `/api/estilos` | Retorna estilos disponíveis |
| `/capas/<nome_arquivo>` | Disponibiliza capas dos jogos |

## 📁 Estrutura do projeto

```text
Projeto-Loki/
├── dados/
│   ├── capas/
│   └── loki.db
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   └── ...
│   └── package.json
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── documentacao/
    └── GUIA_DE_ESTUDO.md
```

## 💻 Executando localmente

### 1. Backend

Na raiz do projeto, crie e ative um ambiente virtual:

```bash
python -m venv venv
```

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie o backend:

```bash
python app.py
```

### 2. Frontend

Em outro terminal:

```bash
cd frontend
npm install
npm run dev
```

Acesse o endereço local informado pelo Vite no terminal.

## 🚀 Implantação

A aplicação está hospedada na Render em dois serviços:

- **Static Site:** frontend desenvolvido em Vue.js.
- **Web Service:** backend desenvolvido em Flask.

O frontend utiliza a variável de ambiente `VITE_API_URL` para localizar a API.

O backend utiliza `FRONTEND_URL` para configurar a origem permitida pelo CORS.

## 📚 Documentação

Para conhecer melhor a arquitetura, a lógica de identificação, o banco de dados e as decisões de desenvolvimento, consulte:

`documentacao/GUIA_DE_ESTUDO.md`

## 🔮 Melhorias futuras

- Ampliar os filtros de identificação.
- Expandir e enriquecer a base de jogos.
- Aprimorar a experiência de pesquisa.
- Avaliar futuramente a utilização de técnicas de Machine Learning.

---

Desenvolvido como projeto acadêmico de Análise e Desenvolvimento de Sistemas.