# Guia de Estudo — Projeto Loki

**Sistema de identificação de jogos do Super Nintendo**

**Desenvolvedor:** Júlio de Almeida Prazeres  
**Curso:** Análise e Desenvolvimento de Sistemas

---

## 1. Apresentação do projeto

O Projeto Loki é uma aplicação web desenvolvida para ajudar usuários a recordar e identificar jogos clássicos do Super Nintendo Entertainment System (SNES).

O usuário seleciona características relacionadas aos jogos, e o sistema utiliza essas informações para consultar o banco de dados e apresentar resultados compatíveis.

O objetivo foi desenvolver uma aplicação funcional, integrando frontend, backend, banco de dados e hospedagem em nuvem.

## 2. Arquitetura da aplicação

O projeto foi dividido em três partes principais:

### 2.1. Frontend — Vue.js

O frontend é a interface com a qual o usuário interage.

Foi desenvolvido utilizando Vue.js, JavaScript, HTML e CSS, com Vite como ferramenta de desenvolvimento e Vue Router para navegação entre páginas.

Suas responsabilidades incluem:

- Exibir as páginas e os componentes.
- Apresentar o catálogo de jogos.
- Permitir a seleção de características.
- Enviar requisições para o backend.
- Apresentar os resultados recebidos da API.

### 2.2. Backend — Python e Flask

O backend é responsável pelo processamento das requisições e pela comunicação com o banco de dados.

Foi desenvolvido com Python e Flask.

Suas responsabilidades incluem:

- Receber requisições HTTP.
- Processar os filtros selecionados.
- Consultar o banco SQLite.
- Retornar os resultados em formato JSON.
- Disponibilizar as imagens das capas.

O Flask-CORS permite configurar quais origens podem acessar a API.

O Gunicorn é utilizado para executar a aplicação no ambiente de produção.

### 2.3. Banco de dados — SQLite

O SQLite foi utilizado para armazenar as informações dos jogos.

A base possui 272 jogos cadastrados e utiliza um modelo relacional.

Entre as entidades estão:

- Jogos;
- Desenvolvedoras;
- Tecnologias;
- Regiões;
- Personagens;
- Compositores.

Como um jogo pode estar associado a várias desenvolvedoras, tecnologias ou outras entidades, foram utilizadas tabelas intermediárias para representar esses relacionamentos.

## 3. Como funciona a identificação?

A identificação é realizada por meio de filtros aplicados às características selecionadas pelo usuário.

O funcionamento segue duas regras principais:

**Dentro de uma mesma categoria: OR**

Quando o usuário seleciona mais de uma opção na mesma categoria, o sistema aceita jogos que correspondam a qualquer uma delas.

Exemplo: se forem selecionados dois estilos, o jogo poderá pertencer ao primeiro OU ao segundo.

**Entre categorias diferentes: AND**

Quando existem filtros em categorias diferentes, o jogo precisa atender às condições de todas elas.

Exemplo: o jogo precisa corresponder ao gênero selecionado E à perspectiva escolhida.

**Categorias sem seleção**

Uma categoria sem opções selecionadas não restringe a consulta.

Dessa forma, o sistema consegue reduzir o conjunto de resultados de acordo com as escolhas do usuário.

A primeira versão não utiliza Inteligência Artificial ou Machine Learning. A identificação é baseada em regras de filtragem e consultas ao banco de dados.

## 4. Comunicação entre frontend e backend

A comunicação acontece por meio de uma API REST.

O frontend envia requisições HTTP para os endpoints disponibilizados pelo Flask.

As respostas são retornadas em JSON, formato leve e adequado para a troca de informações entre aplicações.

### Principais rotas

| Endpoint | Responsabilidade |
|---|---|
| `/api/jogos` | Retorna os jogos cadastrados |
| `/api/buscar` | Realiza a busca por características |
| `/api/opcoes` | Retorna opções de características |
| `/api/estilos` | Retorna os estilos disponíveis |
| `/capas/<nome_arquivo>` | Disponibiliza as imagens das capas |

## 5. Páginas da aplicação

O frontend possui cinco páginas principais:

1. **Início:** apresenta o projeto.
2. **Identificar:** permite selecionar características e buscar jogos.
3. **Catálogo:** apresenta os jogos cadastrados.
4. **Sobre:** apresenta informações sobre o projeto.
5. **Contato:** disponibiliza um canal de contato.

A navegação é realizada pelo Vue Router, que permite trocar de página sem precisar recarregar toda a aplicação.

## 6. Coleta e organização dos dados

As informações dos jogos foram obtidas a partir de dados coletados e organizados durante o desenvolvimento.

Os dados passaram por etapas de tratamento e organização antes de serem armazenados no SQLite.

A estrutura relacional permite relacionar os jogos às suas respectivas características e realizar consultas mais organizadas.

## 7. Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Linguagem do backend |
| Flask | Criação da API |
| SQLite | Banco de dados relacional |
| Vue.js | Construção da interface |
| JavaScript | Lógica do frontend |
| Vite | Desenvolvimento e build do frontend |
| Vue Router | Navegação entre páginas |
| Flask-CORS | Controle de acesso entre origens |
| Gunicorn | Servidor de aplicação em produção |
| Git e GitHub | Versionamento e armazenamento do código |
| Render | Hospedagem da aplicação |

## 8. Implantação em nuvem

A aplicação foi publicada na plataforma Render, utilizando dois serviços separados.

**Frontend — Static Site**

Hospeda os arquivos gerados pelo processo de build do Vue/Vite.

**Backend — Web Service**

Executa a aplicação Flask por meio do Gunicorn e disponibiliza os endpoints da API.

A comunicação entre os serviços é configurada por variáveis de ambiente:

- `VITE_API_URL`: endereço da API utilizado pelo frontend.
- `FRONTEND_URL`: origem autorizada pelo backend no CORS.

O banco SQLite e as imagens das capas são disponibilizados junto ao projeto.

Como a hospedagem utiliza o plano gratuito, o backend pode entrar em inatividade e precisar de alguns segundos para responder à primeira requisição.

## 9. Executando o projeto localmente

### Backend

Na pasta principal do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

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

### Frontend

Em outro terminal:

```bash
cd frontend
npm install
npm run dev
```

O Vite apresentará o endereço local para acessar a aplicação.

## 10. Aprendizados e conhecimentos aplicados

Durante o desenvolvimento foram trabalhados conceitos importantes de Análise e Desenvolvimento de Sistemas:

- Organização e estruturação de projetos.
- Programação com Python e JavaScript.
- Desenvolvimento de aplicações web.
- Criação e consumo de APIs REST.
- Modelagem e consultas em banco de dados relacional.
- Relacionamentos entre entidades.
- Integração entre frontend e backend.
- Versionamento com Git e GitHub.
- Build e implantação em nuvem.
- Resolução de problemas de integração e compatibilidade.

## 11. Possibilidades de evolução

O Projeto Loki foi desenvolvido como uma primeira versão funcional. Entre as possibilidades de evolução estão:

- Ampliar a quantidade de jogos cadastrados.
- Adicionar novas características para identificação.
- Melhorar os filtros e a experiência de pesquisa.
- Aprimorar a organização e a apresentação do catálogo.
- Avaliar a aplicação de técnicas de Machine Learning em versões futuras.

---

**Projeto Loki — Sistema de identificação de jogos do Super Nintendo.**