import ventanas as v
import agregando_mensaje as ag
import construir_ventana_main as m

from tkinter import messagebox

import db as b 
import pygame as p
p.init()
info = p.display.Info()
ancho = info.current_w
alto = info.current_h
def regresar(ventana):
    
    ventana.destroy()
    m.ventana_inicial()
def ventanaAgregar(ventana_main):
    ventana_main.destroy()
    def enviar(anio, mes, dia, mensaje, id_, ventana):
        mensaje = mensaje.get()
        anio = anio.get()
        mes = mes.get()
        dia = dia.get()   
        if mensaje and anio and mes and dia:      
           ag.subiendo(anio, mes, dia, mensaje, id_) 
        else:
            messagebox.showinfo("Error", "Faltan campos por llenar")
        
        regresar(ventana)
        
        

    def agregando(celular, id_):
        
        ventana_mostrar.destroy()
        
        global ventana_agregar
        ventana_agregar = v.MiVentana("Agregando datos", "#102356")
        fuente_personalizada = ("Times New Roman", 12)#fuente y tamaño de la letra para botones
        fuente_texto = ("Arial", 12)
        ventana_agregar.boton_regresar = v.tk.Button(ventana_agregar, text="Regresar al menu", command=lambda: regresar(ventana_agregar), font = fuente_personalizada, width=20, height=5, bg = "#BBD631")
        ventana_agregar.boton_regresar.place(x=ancho-ancho+20, y=alto-alto+20)
        #label 
        ventana_agregar.generarLabel(f"Celular ({celular})", fuente_personalizada, 28, 3, "#009aff", "sunken", 2, 500, 100)

        #label y entry año
        anio = v.tk.StringVar()
        ventana_agregar.generarLabel("Año de envio", fuente_personalizada, 12, 3, "#009aff", "sunken", 2, 500, 200)
        ventana_agregar.generarEntry(fuente_texto, "white", "black", "left", "#47BC1B", "ridge", ancho-ancho +700, alto-alto+210, 100, 50, anio)
        
        #label y entry mes
        mes = v.tk.StringVar()
        ventana_agregar.generarLabel("Mes de envio\n(1-12)", fuente_personalizada, 12, 3, "#009aff", "sunken", 2, 500, 300)
        ventana_agregar.generarEntry(fuente_texto, "white", "black", "left", "#47BC1B", "ridge", ancho-ancho +700, alto-alto+310, 100, 50, mes)

        #label y entry dia
        dia = v.tk.StringVar()
        ventana_agregar.generarLabel("Dia de envio", fuente_personalizada, 14, 3, "#009aff", "sunken", 2, 500, 400)
        ventana_agregar.generarEntry(fuente_texto, "white", "black", "left", "#47BC1B", "ridge", ancho-ancho +700, alto-alto+420, 100, 50, dia)

        #label y mensaje
        mensaje = v.tk.StringVar()
        ventana_agregar.generarLabel("Mensaje", fuente_personalizada, 12, 3, "#009aff", "sunken", 2, 500, 500)
        ventana_agregar.generarEntry(fuente_texto, "white", "black", "left", "#47BC1B", "ridge", ancho-ancho +700, alto-alto+510, 600, 50, mensaje)
        #enviar datos
        ventana_agregar.boton_enviar = v.tk.Button(ventana_agregar, text="Subir datos", command=lambda : enviar(anio, mes, dia, mensaje, id_, ventana_agregar), font = fuente_personalizada, width=20, height=5, bg = "#0a8012")
        ventana_agregar.boton_enviar.place(x=ancho-200, y=alto-alto+20)

        ventana_agregar.mainloop()
    
    def obtenerDatosSeleccionados(event):
        try:
            # Obtenemos el índice de la fila seleccionada
            item = tabla.selection()[0]
            
            # Obtenemos los valores de todas las columnas de esa fila
            valores = tabla.item(item, 'values')
            
            # Los valores de la fila están en la variable 'valores'
            celular = valores[2]
            id_ = valores[0]
            agregando(celular, id_)
        except Exception:
            print(Exception)

    try:
        # Llamar conexión y realizar consulta
        conexion = b.conexion
        cursor = b.cursor
        cursor.execute("SELECT C.ID, C.NOMBRE, C.CELULAR FROM CONTACTOS AS C")
        datos_combinados = cursor.fetchall()
    except Exception as e:
        # Manejo de excepciones en caso de error
        datos_combinados = None

    # Crear ventana
    ventana_mostrar = v.MiVentana("Usuarios, doble click para seleccionar", "#2CCDA1")

    # Verificar si hubo un error en la consulta
    if datos_combinados is None:
        fuente_personalizada = ("Arial", 14)
        mensaje_error = v.tk.Label(ventana_mostrar, text="Error al obtener los datos de la base de datos", font=fuente_personalizada, width=40, height=3, bg="red", relief="sunken", borderwidth=2)
        mensaje_error.pack(padx=20, pady=20)
    else:
        # Crear un frame que contendrá el Treeview y las barras de desplazamiento
        frame = v.ttk.Frame(ventana_mostrar)
        frame.pack(fill="both", expand=True)
        
        # Crear barras de desplazamiento
        yscroll = v.ttk.Scrollbar(frame, orient="vertical")
        xscroll = v.ttk.Scrollbar(frame, orient="horizontal")
        
        # Crear un widget Treeview para mostrar los datos
        tabla = v.ttk.Treeview(frame, columns=("ID", "NOMBRE", "CELULAR"),
                        yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        yscroll.config(command=tabla.yview)
        xscroll.config(command=tabla.xview)

        tabla.heading("#1", text="ID")
        tabla.heading("#2", text="NOMBRE")
        tabla.heading("#3", text="CELULAR")
        
        
        # Llenar la tabla con los datos
        for dato in datos_combinados:
            tabla.insert("", "end", values=dato)
        
        # Configurar el evento de doble clic en la tabla
        tabla.bind("<Double-1>", obtenerDatosSeleccionados)
    
        # Empacar los widgets en el frame
        yscroll.pack(side="right", fill="y")
        xscroll.pack(side="bottom", fill="x")
        tabla.pack(fill="both", expand=True)
    
    ventana_mostrar.mainloop()