import db as d
import webbrowser, pyautogui
import time as t
import pygame as p
from tkinter import messagebox
import speedtest 

conexion = d.conexion
cursor = d.cursor
def revisar_si_mensajes_hoy():
    estructura_tiempo = t.localtime(t.time())
    cursor.execute("SELECT * FROM MENSAJES")
    mensajes = cursor.fetchall()
    fecha_actual = f"{estructura_tiempo.tm_year} {estructura_tiempo.tm_mon} {estructura_tiempo.tm_mday}"
    mensajes_de_hoy = False
    count = 0
    for mensaje in mensajes:
        fecha = f"{mensaje[2]} {mensaje[3]} {mensaje[4]}"
        if fecha_actual == fecha:
            count += 1
    if count != 0:
        mensajes_de_hoy = True
    return mensajes_de_hoy, count
            


def enviar_mensajes():
    p.init()
    p.mixer.init()
    sound = p.mixer.Sound('sonido.mp3')

    estructura_tiempo = t.localtime(t.time())
    diccionario = {}

    try:
        cursor.execute("SELECT * FROM MENSAJES")
        mensajes = cursor.fetchall()
        fecha_actual = f"{estructura_tiempo.tm_year} {estructura_tiempo.tm_mon} {estructura_tiempo.tm_mday}"
        mensajes_de_hoy = False

        #calculo de tiempo si hay mensajes
        if mensajes:
            st = speedtest.Speedtest()
            vel_descarga = st.download() / 10**6  # Convertir a megabits por segundo
            tiempo = 60
            if vel_descarga <=10:
                tiempo = 90
            elif vel_descarga <=20:
                tiempo = 50
            elif vel_descarga <= 50:
                tiempo = 28
            elif vel_descarga <= 100:
                tiempo = 22
            else:
                tiempo = 15
    
            #recopilacion de mensajes
            for mensaje in mensajes:
                fecha = f"{mensaje[2]} {mensaje[3]} {mensaje[4]}"
                if fecha_actual == fecha:
                    cursor.execute("""SELECT C.CELULAR FROM CONTACTOS C
                                    WHERE C.ID = ?""", (mensaje[1], ))
                    celular_destino = cursor.fetchone()
                    id_ = mensaje[0]
                    diccionario[id_] = [celular_destino, mensaje[5]]
                    cursor.execute("DELETE FROM MENSAJES WHERE ID = ?", (id_,))
                    conexion.commit()
                    mensajes_de_hoy = True
            
            
            
            #envio de mensajes
            if mensajes_de_hoy:
                webbrowser.open("https://web.whatsapp.com")
                t.sleep(tiempo+60)
                for clave, valor in diccionario.items():
                    # Escribe la URL con el número de teléfono en la barra de direcciones
                    #pyautogui.click(100, 100)  # Haz clic en la barra de direcciones para seleccionarla
                    pyautogui.hotkey('ctrl', 'l')  # Selecciona la URL actualmente en la barra de direcciones
                    t.sleep(8)
                    pyautogui.press('delete')  # Borra la URL actual
                    t.sleep(8)
                    #                    webbrowser.open("https://web.whatsapp.com/send?phone="+f"{valor[0]}")

                    pyautogui.typewrite("https://web.whatsapp.com/send?phone="+f"{valor[0]}")  # Escribe la nueva URL
                    t.sleep(8)
                    pyautogui.press('enter')  # Presiona Enter para cargar la página
                    t.sleep(tiempo)
                    # Escribe el mensaje
                    pyautogui.typewrite(valor[1])
                    t.sleep(10)
                    # Envía el mensaje
                    pyautogui.press("enter")
                    t.sleep(15)        
        sound.play()
        p.time.wait(int(sound.get_length() * 1000))
        p.quit()
       



    except Exception as e:
        print(e)
        messagebox.showinfo("Error", "Ocurrio un error al enviar los mensajes")
    finally:

        if mensajes_de_hoy == False:
            messagebox.showinfo("Error", "No hay mensajes por enviar hoy")
        elif mensajes_de_hoy == True:
            messagebox.showinfo("Exito","Mensajes enviados")