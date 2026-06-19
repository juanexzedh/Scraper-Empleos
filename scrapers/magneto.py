"""
import requests
from bs4 import BeautifulSoup

url = "https://www.magneto365.com/co/trabajos/buscar/ingenieria-de-software?forwardUrl=aHR0cHM6Ly93d3cubWFnbmV0bzM2NS5jb20vY28vdHJhYmFqb3MvYnVzY2FyL2luZ2VuaWVyaWEtZGUtc29mdHdhcmU%3D"


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
    print(soup.title)
    ofertas = soup.find_all('div', class_="mg_job_card_desktop_magneto-ui-card-jobs_container_13c81")
    print(f"Total de Ofertas: {len(ofertas)}")

else:
    print(f"Hubo un error: {respuesta.status_code}")

#<article class="mg_job_card_desktop_magneto-ui-card-jobs_13c81 mg_job_card_desktop_magneto-ui-card-jobs--urgent_13c81"><div class="mg_job_card_desktop_magneto-ui-card-jobs_data_13c81"><section class="mg_job_card_desktop_magneto-ui-card-jobs_header_13c81"><span class="mg_job_card_desktop_magneto-ui-card-jobs_text_13c81 mg_job_card_desktop_magneto-ui-card-jobs_published_13c81">Hace 8 días</span><section class="mg_job_card_desktop_magneto-ui-card-jobs_options_13c81 opciones"></section></section><h2 class="mg_job_card_desktop_magneto-ui-card-jobs_text_13c81  mg_job_card_desktop_magneto-ui-card-jobs_text--big_13c81 mg_job_card_desktop_magneto-ui-card-jobs_text--bold_13c81"><a href="https://www.magneto365.com/co/empleos/analista-de-desarrollo-de-software-barranquilla-945579" title="Analista De Desarrollo De Software - Barranquilla" target="_blank" rel="noreferrer" class="mg_job_card_desktop_magneto-ui-card-jobs_a_13c81">Analista De Desarrollo De Software - Barranquilla</a></h2><h3 class="mg_job_card_desktop_magneto-ui-card-jobs_text_13c81 ">Confidencial | Por obra o labor</h3><p class="mg_job_card_desktop_magneto-ui-card-jobs_text_13c81 ">Salario a convenir, </p><p class="mg_job_card_desktop_magneto-ui-card-jobs_text_13c81 ">Barranquilla</p></div></article></div>

"""