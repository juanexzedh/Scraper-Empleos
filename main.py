from scrapers.computrabajo import extraer_ofertas_computrabajo
from modelos.database import crear_tabla

crear_tabla()

ofertas = extraer_ofertas_computrabajo()

print(f"Se encontraron {len(ofertas)} ofertas")