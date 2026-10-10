import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

noticias = soup.find_all("article", class_="noticia")

print("=== TODAS AS NOTÍCIAS ===\n")
for noticia in noticias:
    categoria = noticia.find(class_="categoria").get_text(strip=True)
    titulo = noticia.find(class_="titulo").get_text(strip=True)
    data = noticia.find(class_="data").get_text(strip=True)
    resumo = noticia.find(class_="resumo").get_text(strip=True)
    autor = noticia.find(class_="autor").get_text(strip=True)

    print("=" * 50)
    print(f"[{categoria}] {titulo}")
    print(f"Data: {data}")
    print(f"Resumo: {resumo}")
    print(f"{autor}")

print("=" * 50)

categoria_filtro = "Tecnologia"
print(f"\n=== NOTÍCIAS DE {categoria_filtro.upper()} ===\n")
for noticia in noticias:
    categoria = noticia.find(class_="categoria").get_text(strip=True)
    if categoria == categoria_filtro:
        titulo = noticia.find(class_="titulo").get_text(strip=True)
        print(f"  - {titulo}")
