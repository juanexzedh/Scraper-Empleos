import requests
from bs4 import BeautifulSoup

url = "https://co.computrabajo.com/trabajo-de-ingeniero-en-sistemas#D52F94107835024461373E686DCF3405"

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

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    ofertas = soup.find_all('article', class_="box_offer")
    print(soup.title)
    print(f"Total de Ofertas encontradas: {len(ofertas)}")
    cont = 1

    """
    for oferta in ofertas:
        #Extraer titulo de la oferta
        titulo = oferta.find("h2").find("a").get_text(strip=True)
        #Extraer Empresa
        empresa_tag = oferta.find("p", class_="dFlex vm_fx fs16 fc_base mt5")
        if empresa_tag:
            empresa_name = empresa_tag.find("a")
            if empresa_name:
                empresa = empresa_name.get_text(strip=True)#Nombre dentro de <a>
            else:
                empresa = empresa_tag.get_text(strip=True)#Nombre dentro de <p>
        else:
            empresa = "No especificada"
        #Extraer ubicacion
        ciudad = oferta.find("p", class_="fs16 fc_base mt5").span.get_text(strip=True)
        #Extraer Salario
        salario_tag = oferta.find("span", class_="dIB mr10") #El bloque de salario completo
        salario = salario_tag.get_text(strip=True) if salario_tag else None #El "salario" como texto
        #Link de la oferta
        link= oferta.find("a", class_="js-o-link")["href"]
        complete_url = "https://co.computrabajo.com"+link

        print(f"Oferta {cont}:")
        print(f"Titulo:{titulo} \nEmpresa: {empresa} \nCiudad: {ciudad} \nSalario:{salario} \nEnlace: {link} \nURL: {complete_url}")
        cont+=1
    """
    oferta_prueba = ofertas[0]
    enlace_oferta_prueba = "https://co.computrabajo.com"+oferta_prueba.find("a", class_="js-o-link")["href"]
    otra_respuesta = requests.get(enlace_oferta_prueba, headers=headers, timeout=10)
    print(otra_respuesta.status_code)

    soup_oferta1 = BeautifulSoup(otra_respuesta.text, 'html.parser')
    print(soup_oferta1.title)

    #obtener descripcion
    description_tag = soup_oferta1.find("p", class_="mbB")
    if description_tag:
        descripcion = description_tag.get_text(separator="\n", strip=True)
    else:
        descripcion = description_tag.get_text(strip=True)

    #Requerimientos
    req_container = soup_oferta1.find("ul", class_="disc mbB")
    if req_container:
        elementos_req = req_container.find_all("li")
        requerimientos = "\n".join([f"- {li.get_text(strip=True)}" for li in elementos_req])
    else:
        requerimientos = "No especificados"

    #palabras clave
    tags_tag = soup_oferta1.find("p", class_="fc_aux fs13 mbB mtB")
    if tags_tag:
        palabras_clave = tags_tag.get_text(strip=True).replace("Palabras clave:", "").strip()
    else:
        palabras_clave = "Ninguna"

    print(f"Descripcion: {descripcion}")
    print(f"Requerimientos: {requerimientos}")
    print(f"Palabras Clave: {palabras_clave}")

else:
    print(f"Hubo un error: {respuesta.status_code}")


"""
id
fuente
titulo
empresa
ciudad
salario
descripcion
requerimientos
palabras_clave
fecha_publicacion
url
"""
