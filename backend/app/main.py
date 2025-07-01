from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from app.resolvers import resolve_suggestions
from app.trie import autocomplete_trie
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

with open("app/schema.graphql", "r", encoding="utf-8") as f:
    type_defs = f.read()

query = QueryType()
query.set_field("suggestions", resolve_suggestions)
schema = make_executable_schema(type_defs, query)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Carregando dados na Trie...")
    autocomplete_trie.load_from_json("Scraper/glossario_cnmp.json")
    print("Trie inicializada com sucesso!")
    yield
    print("Encerrando aplicação...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/graphql", GraphQL(schema, debug=True))