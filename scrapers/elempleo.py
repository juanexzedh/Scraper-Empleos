"""
import requests
from bs4 import BeautifulSoup
import re

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
    ofertas = soup.find_all('div', class_="col-md-12 result-item mb-3 bg-white")
    print(soup.title)
    print(f"Total de Ofertas encontradas: {len(ofertas)}")
    cont = 1

    for oferta in ofertas:
        #Extraer titulo de la oferta
        titulo = oferta.find("h2").find("a").get_text(strip=True)
        #Extraer Empresa
        empresa_tag = oferta.find("span", class_="info-company-name js-offer-company fs-6 two-lines text-blue-petrol-dark")
        if empresa_tag:
            empresa = empresa_tag.get_text(strip=True)
        else:
            empresa = "No especificada"
        #Extraer ubicacion
        ciudad = oferta.find("span", class_="info-city js-offer-city text-blue-petrol-dark").span.get_text(strip=True)

        #Extraer Salario
        salario_tag = oferta.find("div", class_="text-blue-petrol-dark").get_text()
        

        #Link de la oferta

        print(f"Oferta {cont}:")
else:
    print(f"Hubo un error: {respuesta.status_code}")

"""