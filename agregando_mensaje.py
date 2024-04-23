import db as b
import ventanas as v
from tkinter import messagebox
def subiendo(anio, mes, dia, mensaje, id_):
   

    try:
        conexion = b.conexion
        cursor = b.cursor
        cursor.execute("INSERT INTO MENSAJES (CONTACTO_ID, ANIO, MES, DIA, MENSAJE) VALUES (?, ?, ?, ?, ?)", (id_, anio, mes, dia, mensaje))
        conexion.commit()

        messagebox.showinfo("Exito", "Datos subidos correctamente.")
    except Exception as e:
       
        messagebox.showinfo("Error", "Error vuelva a internarlo mas tarde :(")


    
