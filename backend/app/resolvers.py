
from app.trie import autocomplete_trie
from typing import Any, List, Dict

async def resolve_suggestions(_ : Any, info: Any, term: str) -> List[Dict[str, Any]]:
    """Resolver para buscar sugestões usando a Trie"""
    if len(term) < 4:
        return []
    
    results = autocomplete_trie.search_prefix(term, limit=20)
    return results