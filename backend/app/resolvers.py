# app/resolvers.py
from app.trie.loader import load_trie_from_json

# Carrega a Trie na inicialização do módulo (uma única vez)
trie = load_trie_from_json("Scraper/glossario_cnmp.json")

async def resolve_suggestions(_, info, term):
    if len(term) < 4:
        return []
    resultados = trie.search_prefix(term, limit=20)
    return [{"id": i, "text": termo} for i, termo in enumerate(resultados)]
