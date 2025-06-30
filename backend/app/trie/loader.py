# app/trie/loader.py
import json
from .trie import Trie

def load_trie_from_json(path: str) -> Trie:
    trie = Trie()
    with open(path, "r", encoding="utf-8") as f:
        termos = json.load(f)
    for termo in termos:
        trie.insert(termo)
    return trie
