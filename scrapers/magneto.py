import requests
from bs4 import BeautifulSoup

url = "https://www.elempleo.com/co/ofertas-empleo/trabajo-ingeniero-de-sistemas"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,"
        "application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "es-CO,es;q=0.9,en;q=0.8",
    "Referer": "https://www.google.com/",
}

respuesta = requests.get(url, headers=headers, timeout=10)
print(respuesta.status_code)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    ofertas = soup.find_all('article', class_="box_offer")
    print(soup.title)
    print(f"Total de Ofertas encontradas: {len(ofertas)}")

else:
    print(f"Hubo un error: {respuesta.status_code}")
