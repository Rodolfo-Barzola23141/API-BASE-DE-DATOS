import sqlite3

DATABASE_NAME = "mydatabase.db"

def check_connection():
    try:
        sqlite3.connect(DATABASE_NAME).close()
        return {"status": "success", "message": "Conexión a la base de datos exitosa."}
    except sqlite3.Error as e:
        return {"status": "error", "message": f"Error al conectar a la base de datos: {e}"}