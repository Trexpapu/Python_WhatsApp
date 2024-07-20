import ventanas as v
import mostrando_mensajes as mosdb
import auto
from tkinter import messagebox
import agregar_contacto as agre_c 
import mostrar_contactos as mc
import pygame as p
import ventana_agregar_mensajes as va
p.init()
info = p.display.Info()
ancho = info.current_w
alto = info.current_h
def ModificarEliminar():
    mosdb.mostrarDatos()


def agregar_contacto():
    agre_c.formulario()

def borrar_o_modificar_contacto():
    mc.formulario()

def ventana_inicial():
        global ventanaInicial
        
        ventanaInicial = v.MiVentana("MENU", "#102356")#creando objeto ventana
        fuente_personalizada = ("Times New Roman", 10)#fuente y tamaño de la letra para botones
        ventanaInicial.crear_contacto = v.tk.Button(ventanaInicial, text="Agregar contacto", command=agregar_contacto, width=32, height=3, bg = "#009aff", font=fuente_personalizada)
        ventanaInicial.crear_contacto.place(x = ancho-400, y = alto-600)
        ventanaInicial.modificar_contacto = v.tk.Button(ventanaInicial, text="Modificar o eliminar contacto", command=borrar_o_modificar_contacto, width=32, height=3, bg = "#009aff", font=fuente_personalizada)
        ventanaInicial.modificar_contacto.place(x = ancho-400, y = alto-500)
        ventanaInicial.agregar_boton = v.tk.Button(ventanaInicial, text="Programar mensajes", command=lambda: va.ventanaAgregar(ventanaInicial), width=32, height=3, bg="#009aff", font = fuente_personalizada)#creacion de boton agregar datos
        ventanaInicial.agregar_boton.place(x = ancho-400, y = alto-400)#posicion de boton agregar datos
        ventanaInicial.modificar_eliminar_boton = v.tk.Button(ventanaInicial, text="Modificar o eliminar mensaje programado", command=ModificarEliminar, width=32, height=3, bg="#009aff", font = fuente_personalizada)#boton modificar o eliminar datos
        ventanaInicial.modificar_eliminar_boton.place(x = ancho-400, y = alto-300)#posicion del boton modificar o eliminar datoss
        ventanaInicial.modificar_eliminar_boton = v.tk.Button(ventanaInicial, text="Enviar mensajes de hoy", command=auto.enviar_mensajes, width=32, height=3, bg="#009aff", font = fuente_personalizada)#boton modificar o eliminar datos
        ventanaInicial.modificar_eliminar_boton.place(x = ancho-400, y = alto- 200)#posicion del enviar mensaje
        imagen = v.Image.open("logo1.png")
        if ancho <= 800:
            imagen = imagen.resize((1, 1), v.Image.ANTIALIAS)
        else:
            imagen = imagen.resize((ancho//2, alto-200), v.Image.ANTIALIAS)
        imagen_tk = v.ImageTk.PhotoImage(imagen)

        etiqueta = v.tk.Label(ventanaInicial, image=imagen_tk)
        etiqueta.place(x=ancho - ancho + 10, y=alto - alto + 100)


        mensajes_hoy, contador = auto.revisar_si_mensajes_hoy()
        if mensajes_hoy:
            messagebox.showinfo("Saludos", f"Hay {contador} mensajes por enviar el dia de hoy")
        ventanaInicial.mainloop()#LOOP de la ventana inicial 