import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

secoes = soup.find_all("section", class_="secao")

for secao in secoes:
    categoria = secao.find(class_="categoria").get_text(strip=True)
    print(f"\n{'=' * 40}")
    print(f"  {categoria.upper()}")
    print(f"{'=' * 40}")

    itens = secao.find_all("div", class_="item")
    for item in itens:
        nome = item.find(class_="nome").get_text(strip=True)
        descricao = item.find(class_="descricao").get_text(strip=True)
        preco = item.find(class_="preco").get_text(strip=True)

        print(f"\n  {nome}")
        print(f"  {descricao}")
        print(f"  Preço: {preco}")

print()
