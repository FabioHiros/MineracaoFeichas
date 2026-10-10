import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

livros = soup.find_all("div", class_="livro")

print("=== TODOS OS LIVROS ===\n")
for livro in livros:
    titulo = livro.find(class_="titulo").get_text(strip=True)
    autor = livro.find(class_="autor").get_text(strip=True)
    ano = livro.find(class_="ano").get_text(strip=True)
    genero = livro.find(class_="genero").get_text(strip=True)
    situacao = livro.find(class_="situacao").get_text(strip=True)
    palavras = [li.get_text(strip=True) for li in livro.find("ul", class_="palavras-chave").find_all("li")]

    print("-" * 40)
    print(f"Título:    {titulo}")
    print(f"{autor}")
    print(f"{ano}")
    print(f"{genero}")
    print(f"Situação:  {situacao}")
    print(f"Palavras-chave: {', '.join(palavras)}")

print("-" * 40)

print("\n=== LIVROS DISPONÍVEIS ===\n")
for livro in livros:
    situacao = livro.find(class_="situacao").get_text(strip=True)
    if situacao == "Disponível":
        titulo = livro.find(class_="titulo").get_text(strip=True)
        autor = livro.find(class_="autor").get_text(strip=True)
        print(f"  {titulo} — {autor}")
