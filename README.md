# Autocomplete - Guia de Instalação e Execução

Este projeto é um sistema de autocomplete com back-end em FastAPI + GraphQL e front-end em React, utilizando uma Trie para buscas rápidas. Abaixo estão as instruções para rodar o projeto localmente usando Docker.

## Pré-requisitos

- [Docker](https://www.docker.com/get-started) instalado
- [Docker Compose](https://docs.docker.com/compose/) instalado

## Passos para rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd AutoComplete
   ```

2. **Suba os containers:**
   ```bash
   docker-compose up --build
   ```
   Isso irá construir e iniciar tanto o back-end quanto o front-end.

3. **Acesse a aplicação:**
   - Front-end: [http://localhost:3000](http://localhost:3000)
   - Back-end (GraphQL Playground): [http://localhost:8000/graphql](http://localhost:8000/graphql)

## Estrutura do Projeto

- `backend/`: Código do back-end (FastAPI, Ariadne, Trie, Scraper)
- `frontend/autocomplete/`: Código do front-end (React)

## Observações
- O sistema já vem com um arquivo de dados para a Trie, carregado automaticamente ao iniciar o back-end.
- Para parar os containers, use `Ctrl+C` no terminal ou rode `docker-compose down`.
- Se quiser rodar apenas o back-end ou o front-end, ajuste o `docker-compose.yml` conforme necessário.

## Possíveis problemas
- Certifique-se de que as portas 3000 (front) e 8000 (back) estejam livres.

---

