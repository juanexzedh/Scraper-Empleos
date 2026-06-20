import sqlite3
import os

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


def obtener_total_ofertas():
    conexion = sqlite3.connect("data/empleos.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM empleos")
    total = cursor.fetchone()[0]

    conexion.close()
    return total

def obtener_empresas_top():
    conexion = sqlite3.connect("data/empleos.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM empleos")
    total = cursor.fetchone()[0]

    conexion.close()
    return total

def obtener_ciudades_top():


def obtener_salario_promedio():


def buscar_por_palabra_clave():


