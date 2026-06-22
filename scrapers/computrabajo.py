import requests, sys, io, time
from bs4 import BeautifulSoup
from datetime import datetime

def extraer_ofertas_computrabajo(paginas=5): # Parametro con valor por defecto
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # URL BASE para los cambios entre paginas
    url_base = "https://co.computrabajo.com/trabajo-de-ingeniero-en-sistemas"

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

    fecha_scrapeo = datetime.now().strftime('%Y-%m-%d')
    ofertas_estructuradas = []
    cont = 1

    #Bucle para iterar entre paginas
    for p in range(1, paginas + 1):
        url = f"{url_base}?p={p}" # <-- La url acaba o refiere a la pagina que scrapea

        respuesta = requests.get(url, headers=headers, timeout=10)

        if respuesta.status_code == 200:
            respuesta.encoding = respuesta.apparent_encoding
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            ofertas = soup.find_all('article', class_="box_offer")
            
            # si llega a una página vacia, detiene el bucle
            if not ofertas:
                break

            print(soup.title)
            print(f"Total de Ofertas encontradas en pág {p}: {len(ofertas)}")
            print(f"Fecha del Scrapping: {fecha_scrapeo}")

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
                        empresa = "No especificada"
                else:
                    empresa = "No especificada"

                #Extraer ubicacion
                ciudad = oferta.find("p", class_="fs16 fc_base mt5").span.get_text(strip=True)

                #Extraer Salario
                salario_tag = oferta.find("span", class_="dIB mr10") #El bloque de salario completo
                if salario_tag:
                    salario_texto = salario_tag.get_text(strip=True)
                    try:
                        # Dejar solo números, puntos y comas y reemplazar el $ y cualquier espacio, y dividir en el paréntesis
                        solo_numeros = salario_texto.split('(')[0].replace('$', '').strip()
                        # Quitar los puntos de los miles -> "2000000,00"
                        # Cambiar la coma decimal por un punto -> "2000000.00"
                        numero_formateado = solo_numeros.replace('.', '').replace(',', '.')
                        
                        # Convertir a tipo numerico -> 2000000.0 (float)
                        salario_numerico = float(numero_formateado)
                        
                    except (ValueError, IndexError):
                        # si ocurre un error
                        salario_numerico = None
                else:
                    salario_numerico = None


                #Link de la oferta
                link= oferta.find("a", class_="js-o-link")["href"]
                complete_url = "https://co.computrabajo.com"+link

                #Publicacion
                publicacion = oferta.find("p", class_="fs13 fc_aux mt15").get_text(strip=True)


                #ESPECIFICACIONES DE CADA OFERTA (otro requests)
                otra_respuesta = requests.get(complete_url, headers=headers, timeout=10)
                soup_oferta_i = BeautifulSoup(otra_respuesta.text, 'html.parser')

                #obtener descripcion
                description_tag = soup_oferta_i.find("p", class_="mbB")
                if description_tag:
                    descripcion = description_tag.get_text(separator="\n", strip=True)
                else:
                    descripcion = "No especifica"

                #Requerimientos
                req_container = soup_oferta_i.find("ul", class_="disc mbB")
                if req_container:
                    elementos_req = req_container.find_all("li")
                    requerimientos = "\n".join([f"- {li.get_text(strip=True)}" for li in elementos_req])
                else:
                    requerimientos = "No especificados"

                #palabras clave
                tags_tag = soup_oferta_i.find("p", class_="fc_aux fs13 mbB mtB")
                if tags_tag:
                    palabras_clave = tags_tag.get_text(strip=True).replace("Palabras clave:", "").strip()
                else:
                    palabras_clave = "Ninguna"


                #CREACION DE UN DICCIONARIO PARA CADA OFERTA
                ofertas_dict = {
                    "fuente": "Computrabajo",
                    "titulo": titulo,
                    "empresa": empresa,
                    "ciudad": ciudad,
                    "salario": salario_numerico,
                    "descripcion": descripcion,
                    "requerimientos": requerimientos,
                    "palabras_clave": palabras_clave,
                    "fecha_publicacion": publicacion,
                    "fecha_scraping" : fecha_scrapeo,
                    "url": complete_url
                }
                ofertas_estructuradas.append(ofertas_dict)
                cont+=1
                
                time.sleep(0.5) # Pausa minima anti-bloqueo entre ofertas individuales

            time.sleep(2) # Pausa anti-bloqueo entre paginas completas
        else:
            return f"Hubo un error: {respuesta.status_code}"
            
    return ofertas_estructuradas
    
