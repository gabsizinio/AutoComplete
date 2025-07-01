import json
from typing import List, Dict, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.word_id: Optional[int] = None
        self.full_text: Optional[str] = None
        self.all_terms: List[str] = []


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_counter = 0

    def insert(self, word: str) -> int:
        """Insere uma palavra na Trie e retorna o ID atribuído"""
        node = self.root
        word_lower = word.lower()
        
        for char in word_lower:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        if not node.is_end_of_word:
            self.word_counter += 1
            node.word_id = self.word_counter
            node.full_text = word
            node.is_end_of_word = True
        
        return node.word_id

    def search_prefix(self, prefix: str, limit: int = 20) -> List[Dict[str, any]]:
        """Busca todas as palavras que começam com o prefixo dado"""
        if len(prefix) < 4:
            return []
            
        node = self.root
        prefix_lower = prefix.lower()
        
        # Navega até o nó do prefixo
        for char in prefix_lower:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Coleta todas as palavras que começam com o prefixo
        results = []
        self._collect_words(node, results, limit)
        
        return results[:limit]

    def _collect_words(self, node: TrieNode, results: List[Dict[str, any]], limit: int):
        """Coleta recursivamente todas as palavras a partir de um nó"""
        if len(results) >= limit:
            return
            
        if node.is_end_of_word:
            results.append({
                "id": str(node.word_id),
                "text": node.full_text
            })
        
        for child in node.children.values():
            if len(results) >= limit:
                break
            self._collect_words(child, results, limit)

    def load_from_json(self, json_file_path: str):
        """Carrega palavras de um arquivo JSON"""
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                termos = json.load(f)
            
            for termo in termos:
                self.insert(termo)
                
            self.all_terms = termos

            print(f"Carregados {len(termos)} termos na Trie")
        except FileNotFoundError:
            print(f"Arquivo {json_file_path} não encontrado")
        except json.JSONDecodeError:
            print(f"Erro ao decodificar JSON do arquivo {json_file_path}")

# Instância global da Trie
autocomplete_trie = Trie()