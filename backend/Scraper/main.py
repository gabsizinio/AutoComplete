import requests
from bs4 import BeautifulSoup
import time
import json
from urllib.parse import urljoin

'''

Objetivo

Fazer scraping do glossário do CNMP, coletando todos os termos listados de A até Z, percorrendo todas as páginas de cada letra, e salvando os termos num arquivo .json.

Estrutura do código

1. get_letras()

    Abre a primeira página (?filter-search-alf=A) para capturar todos os links das letras (A, B, C... Z).

    Dentro da <div class="div-letras">, ele coleta os <a href="..."> de cada letra.

    Usa urljoin() para montar o link absoluto da letra (ex: https://www.cnmp.mp.br/portal/glossario?filter-search-alf=B&limitstart=0).

2. get_termos_por_letra(url)

    Acessa a URL inicial da letra.

    Dentro da <div class="groupItems">, pega todos os <li><strong>TERMO</strong></li> e extrai o texto.

    Procura dentro da <div class="pagination"> o link do botão "Próxima" (se existir).

    Se achar, atualiza a url e continua a iteração.

    Quando o botão não estiver mais lá, ele para.

3. Loop principal

    Percorre os links de todas as letras (de get_letras()).

    Para cada uma, chama get_termos_por_letra().

    Adiciona os termos extraídos num set (todos_termos) para evitar duplicatas.

4. Salvamento

    Ao final, salva todos os termos únicos no arquivo glossario_cnmp.json.

requests                Faz requisições HTTP para baixar o HTML das páginas
bs4 (BeautifulSoup)	    Analisa o HTML recebido e permite navegar e extrair dados
json	                Salva os dados coletados no formato JSON
time	                Dá pausas entre as requisições (evita sobrecarregar o servidor)
urllib.parse.urljoin	Garante a construção correta das URLs a partir de hrefs relativos

'''


BASE_URL = "https://www.cnmp.mp.br"
START_URL = f"{BASE_URL}/portal/glossario?filter-search-alf=A&limitstart=0"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_letras():
    response = requests.get(START_URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    letras = []

    div_letras = soup.find("div", class_="div-letras")
    if div_letras:
        for li in div_letras.find_all("li"):
            a = li.find("a")
            if a and "href" in a.attrs:
                letras.append(urljoin(BASE_URL, a["href"]))
    return letras

def get_termos_por_letra(url):
    """Coleta todos os termos de uma letra específica"""
    termos = set()
    while url:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # Coletar termos
        group = soup.find("div", class_="groupItems")
        if group:
            for li in group.find_all("li"):
                strong = li.find("strong")
                if strong:
                    termo = strong.get_text(strip=True)
                    termos.add(termo)

        # Verificar se há uma próxima página
        pagination = soup.find("div", class_="pagination")
        next_link = None

        if pagination:
            next_li = pagination.find("li", class_="pagination-next")
            if next_li and next_li.find("a"):
                href = next_li.find("a")["href"]
                next_link = BASE_URL + href

        url = next_link
        time.sleep(1)  # evita sobrecarregar o site
    return termos

# Rodar o scraping de A a Z
todos_termos = set()
links_por_letra = get_letras()

for letra_url in links_por_letra:
    print(f"Processando: {letra_url}")
    termos = get_termos_por_letra(letra_url)
    todos_termos.update(termos)

# Salvar em JSON
with open("glossario_cnmp.json", "w", encoding="utf-8") as f:
    json.dump(sorted(list(todos_termos)), f, ensure_ascii=False, indent=2)

print(f"Total de termos coletados: {len(todos_termos)}")
