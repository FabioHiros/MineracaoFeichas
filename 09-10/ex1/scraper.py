import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

cursos = soup.find_all("div", class_="curso")

for curso in cursos:
    nome = curso.find(class_="nome").get_text(strip=True)
    area = curso.find(class_="area").get_text(strip=True)
    carga = curso.find(class_="carga").get_text(strip=True)
    assuntos = [li.get_text(strip=True) for li in curso.find("ul", class_="assuntos").find_all("li")]

    print("=" * 40)
    print(f"Curso: {nome}")
    print(f"{area}")
    print(f"{carga}")
    print("Assuntos:")
    for assunto in assuntos:
        print(f"  - {assunto}")

print("=" * 40)
