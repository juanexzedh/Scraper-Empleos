import sqlite3, os

def conectar_db():
    try:
        #Crear la conexion y la base de datos
        conexion = sqlite3.connect("data/empleos.db")

        #Crear un cursor para usar lenguaje Sql
        cursor = conexion.cursor()
        cursor.execute("SELECT sqlite_version();")
        version = cursor.fetchone() 
        return conexion, cursor
    
    except sqlite3.Error as e:
        return f"Error al conectar a la base de datos: {e}"


def crear_tabla():
    #Crea la tabla donde se almacenaran las ofertas
    conexion, cursor = conectar_db()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fuente TEXT NOT NULL,
                titulo TEXT NOT NULL,
                empresa TEXT NOT NULL,
                ciudad TEXT NOT NULL,
                salario INTEGER,
                descripcion TEXT,
                requerimientos TEXT,
                palabras_clave TEXT,
                fecha_publicacion TEXT NOT NULL,
                fecha_scraping TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE
            );
        """)
    conexion.commit()
    conexion.close()

def insertar_ofertas(lista_ofertas):
    conexion = sqlite3.connect("data/empleos.db")
    cursor = conexion.cursor()

    for oferta in lista_ofertas:
        cursor.execute("""
            INSERT OR REPLACE INTO empleos(
                    fuente,
                    titulo,
                    empresa,
                    ciudad,
                    salario,
                    descripcion,
                    requerimientos,
                    palabras_clave,
                    fecha_publicacion,
                    fecha_scraping,
                    url
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                oferta["fuente"],
                oferta["titulo"],
                oferta["empresa"],
                oferta["ciudad"],
                oferta["salario"],
                oferta["descripcion"],
                oferta["requerimientos"],
                oferta["palabras_clave"],
                oferta["fecha_publicacion"],
                oferta["fecha_scraping"],
                oferta["url"],
            )
            )
    conexion.commit()
    cursor.execute("SELECT * FROM empleos")
    print(cursor.fetchall())
    conexion.close()

#NUMERO DE OFERTAS
def obtener_total_ofertas():
    conexion = sqlite3.connect("data/empleos.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM empleos")
    total = cursor.fetchone()[0]

    conexion.close()
    return total

#EMPRESAS CON MAS OFERTAS
def obtener_empresas_top():
    conexion = sqlite3.connect("data/empleos.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT empresa, COUNT(*)
        FROM empleos
        GROUP BY empresa
        ORDER BY COUNT(*) DESC
        LIMIT 10
    """)

    resultado = cursor.fetchall()

    conexion.close()
    return resultado

#CIUDADES CON MAS OFERTAS
def obtener_ciudades_top():
    conexion = sqlite3.connect("data/empleos.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT ciudad, COUNT(*)
        FROM empleos
        GROUP BY ciudad
        ORDER BY COUNT(*) DESC
        LIMIT 10
    """)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

#SALARIO PROMEDIO
def obtener_salario_promedio():
    conexion = sqlite3.connect("data/empleos.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT AVG(salario) AS promedio FROM empleos")
    promedio = cursor.fetchone()

    conexion.close()
    return promedio

#BUSCADOR POR KEYWORD
def buscar_por_palabra_clave():
    conexion = sqlite3.connect("data/empleos.db")
    cursor = conexion.cursor()

    TECNOLOGIAS = [
        "Python", "Java", "JavaScript", "SQL", "React",
        "Angular", "Docker", "AWS", "Git",".NET", 
        "C#", "Linux", "HTML", "CSS", "PHP",
        "Node.js", "IA", "Docker", "Tailwind", "ApiRest",
        "Json", "Html5", "C#", "C++", "SOAP",
        "RESTFUL", "Windows", "Angular", "Node.js", "Express",
        "TypeScript", "Ruby", "PHP", "Kotlin", 
        "MySQL", "Oracle", "PostgreSQL", "Azure", "Google Cloud",
        "API", "Laravel", "Flask", "Django", "FastAPI", "Spring",
        "XML", "Data Science", "Big Data", "Power BI"
    ]

    cursor.execute("""
        SELECT descripcion, requerimientos, palabras_clave
        FROM empleos
    """)

    ofertas = cursor.fetchall()
    conteo = {}

    for tecnologia in TECNOLOGIAS:
        conteo[tecnologia] = 0 #Se le establece un contador a cada tecnologia o palabra clave

    for descripcion, requerimientos, palabras_clave in ofertas:
        texto = f"{descripcion} {requerimientos} {palabras_clave}".lower() #convierte todo a un texto unico para hacerlo mas facil de analizar
        for tecnologia in TECNOLOGIAS: #por cada palabra clave en la lista de tecnologias
            if tecnologia.lower() in texto: #si la tecnologia (en miniscula) esta en el texto, le añade uno al contador de esa tecnologia
                conteo[tecnologia] += 1

    conexion.close()
    return conteo


