import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

produtos = soup.find_all("div", class_="produto")

print("=== TODOS OS PRODUTOS ===\n")
for produto in produtos:
    nome = produto.find(class_="nome").get_text(strip=True)
    fabricante = produto.find(class_="fabricante").get_text(strip=True)
    categoria = produto.find(class_="categoria").get_text(strip=True)
    preco = produto.find(class_="preco").get_text(strip=True)
    situacao = produto.find(class_="situacao").get_text(strip=True)

    print("-" * 40)
    print(f"Produto:    {nome}")
    print(f"{fabricante}")
    print(f"{categoria}")
    print(f"{preco}")
    print(f"Situação:   {situacao}")

print("-" * 40)

print("\n=== PRODUTOS DISPONÍVEIS ===\n")
for produto in produtos:
    situacao = produto.find(class_="situacao").get_text(strip=True)
    if situacao == "Disponível":
        nome = produto.find(class_="nome").get_text(strip=True)
        preco = produto.find(class_="preco").get_text(strip=True)
        print(f"  {nome} — {preco}")
