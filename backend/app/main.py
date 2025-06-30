# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from app.resolvers import resolve_suggestions

with open("app/schema.graphql", "r", encoding="utf-8") as f:
    type_defs = f.read()

query = QueryType()
query.set_field("suggestions", resolve_suggestions)
schema = make_executable_schema(type_defs, query)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/graphql/", GraphQL(schema, debug=True))
