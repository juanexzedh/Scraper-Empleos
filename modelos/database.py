import sqlite3

try:
    conexion = sqlite3.connect("empleos.db")

    cursor = conexion.cursor()

    cursor.execute("SELECT sqlite_version();")
    version = cursor.fetchone()
    print(f"¡Conexión exitosa! Versión de SQLite: {version[0]}")

    conexion.close()
    
except sqlite3.Error as e:
    print(f"Error al conectar a la base de datos: {e}")

def crear_tabla():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados(
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