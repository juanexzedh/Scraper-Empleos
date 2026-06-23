from scrapers.computrabajo import extraer_ofertas_computrabajo
from modelos.database import crear_tabla, insertar_ofertas, vaciar_tabla_empleos

#vaciar_tabla_empleos() ...si se requiere
crear_tabla()

ofertas = extraer_ofertas_computrabajo()

insertar_ofertas(ofertas)

print(f"Se procesaron {len(ofertas)} ofertas")