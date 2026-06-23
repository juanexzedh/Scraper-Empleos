# Scraper de Empleos TI

## Descripción

Este proyecto permite extraer ofertas de empleo del área de Tecnología de la Información (TI) desde portales de empleo, almacenarlas en una base de datos SQLite y visualizarlas mediante un dashboard web desarrollado con Flask.

Actualmente el sistema implementa un scraper funcional para Computrabajo y está preparado para incorporar nuevas fuentes como Magneto y El Empleo en futuras versiones.

---

## Objetivos

* Automatizar la recolección de ofertas de empleo.
* Almacenar la información en una base de datos local.
* Realizar consultas y análisis sobre las ofertas recopiladas.
* Visualizar métricas relevantes mediante un dashboard interactivo.

---

## Tecnologías Utilizadas

* Python 3
* Requests
* BeautifulSoup4
* SQLite3
* Flask
* Bootstrap 5
* Chart.js

---

## Estructura del Proyecto

```text
SCRAPER-EMPLEOS/
│
├── data/
│   └── empleos.db
│
├── modelos/
│   └── database.py
│
├── scrapers/
│   ├── computrabajo.py
│   ├── magneto.py
│   └── elempleo.py
│
├── static/
│   └── script.js
│
├── templates/
│   ├── index.html
│   └── resultados.html
│
├── dashboard.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Información almacenada

Cada oferta contiene los siguientes campos:

| Campo             | Descripción                         |
| ----------------- | ----------------------------------- |
| id                | Identificador único                 |
| fuente            | Portal de empleo                    |
| titulo            | Nombre de la oferta                 |
| empresa           | Empresa contratante                 |
| ciudad            | Ciudad de la oferta                 |
| salario           | Salario ofrecido                    |
| descripcion       | Descripción del cargo               |
| requerimientos    | Requisitos solicitados              |
| palabras_clave    | Tecnologías o habilidades asociadas |
| fecha_publicacion | Fecha de publicación                |
| fecha_scraping    | Fecha de extracción                 |
| url               | Enlace directo a la oferta          |

---

## Funcionalidades

### Scraping

* Extracción automática de ofertas desde Computrabajo.
* Extracción de información detallada de cada oferta.
* Conversión de salarios a formato numérico.
* Normalización de caracteres especiales.

### Base de Datos

* Almacenamiento persistente mediante SQLite.
* Inserción automática de ofertas.
* Actualización de registros existentes mediante URL única.

### Dashboard

* Total de ofertas registradas.
* Salario promedio.
* Empresas que más contratan.
* Tecnologías más demandadas.
* Visualización gráfica de tecnologías.
* Consulta de ofertas almacenadas.

### Buscador

Permite buscar ofertas relacionadas con una tecnología específica.

Ejemplos:

* Python
* Java
* SQL
* Docker
* React
* AWS

---

## Instalación

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar el scraper:

```bash
python main.py
```

4. Ejecutar el dashboard:

```bash
python dashboard.py
```

5. Abrir el navegador:

```text
http://127.0.0.1:5000
```

---

## Posibles Mejoras Futuras

* Integración completa con Magneto.
* Integración completa con El Empleo.
* Extracción de múltiples páginas de resultados.
* Dashboard con más métricas.
* Exportación a Excel y CSV.
* Despliegue en la nube.
* Automatización mediante tareas programadas.

---

## Autor
Juan Esteban Hernández Gualtero
Proyecto desarrollado como parte de una práctica académica de análisis y visualización de ofertas laborales en el sector TI.
