import sqlite3 as sql#importamos sqlite3
try:#creamos un try para manejo de errores
    conexion = sql.connect("USUARIOS_WP")#creacion de la db con nombre USUARIOS_WP
    cursor = conexion.cursor()#creacion de obtejo tipo cursor para usar comandos sql
    cursor.execute("CREATE TABLE IF NOT EXISTS CONTACTOS(ID INTEGER PRIMARY KEY, NOMBRE TEXT, CELULAR TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS MENSAJES(ID INTEGER PRIMARY KEY, CONTACTO_ID INTEGER, ANIO TEXT, MES TEXT, DIA TEXT, MENSAJE TEXT, FOREIGN KEY(CONTACTO_ID) REFERENCES CONTACTOS(ID))")#creacion de tabla mensajes
    conexion.commit()#guardando cambios
except sql.Error as e:#manejo de errores si es que hay uun error de conexion
    print("Error de sql", e)

