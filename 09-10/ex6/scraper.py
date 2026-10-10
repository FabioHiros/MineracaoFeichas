import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

eventos = soup.find_all("div", class_="evento")

print("=== AGENDA DE EVENTOS ===\n")
for evento in eventos:
    nome = evento.find(class_="nome").get_text(strip=True)
    data = evento.find(class_="data").get_text(strip=True)
    horario = evento.find(class_="horario").get_text(strip=True)
    local = evento.find(class_="local").get_text(strip=True)
    palestrantes = [p.get_text(strip=True) for p in evento.find_all(class_="palestrante")]
    link = evento.find("a", class_="inscricao")
    link_texto = link.get_text(strip=True)
    link_href = link["href"]

    print("=" * 50)
    print(f"Evento:    {nome}")
    print(f"{data}")
    print(f"{horario}")
    print(f"{local}")
    if len(palestrantes) > 1:
        print(f"Palestrantes ({len(palestrantes)}): {', '.join(palestrantes)}  [** Múltiplos palestrantes **]")
    else:
        print(f"Palestrante: {palestrantes[0]}")
    print(f"Inscrição: {link_texto} → {link_href}")

print("=" * 50)
