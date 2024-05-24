import tkinter as tk
from tkinter import messagebox
import shutil
import subprocess
import os
import signal
import time
import pyautogui
import win32gui

# Abrimos el launcher de Minecraft Java
os.popen('C:/Users/osnir/AppData/Roaming/.minecraft/TLauncher.exew')
time.sleep(3)

# rutas de las carpetas a mover
carpeta_Vanilla = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/Servidores/Vanilla"
carpeta_Mi_Survival = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/Servidores/Mi Survival"
carpeta_Caballeros = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/Servidores/Caballeros"
carpeta_Carpeta4 = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/Servidores/Carpeta 4"

Carpeta_Destino = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/mods"


def minecraft_primer_plano():
    # Obtener el identificador de la ventana
    hwnd = win32gui.FindWindow(None, 'TLauncher 2.879')
    # Poner la ventana en primer plano
    win32gui.SetForegroundWindow(hwnd)

# Comprobar si existe la carpeta para eliminarla primero


def si_existe_carpeta():
    if os.path.exists(Carpeta_Destino):
        # borra el contenido de la carpeta
        shutil.rmtree(Carpeta_Destino)
        ruta_carpeta = os.path.join(
            "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)", "mods")
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)


def cerrar_minecraft():
    # iniciar el proceso del programa
    proceso = subprocess.Popen("javaw.exe")
    # obtener el ID del proceso
    pid = proceso.pid
    # cerrar el programa
    os.kill(pid, signal.SIGTERM)

# función a ejecutar cuando se presiona el botón 1


def Vanilla():
    si_existe_carpeta()
    ventana.destroy()
    minecraft_primer_plano()
    # crear una ventana principal
    root = tk.Tk()
    root.withdraw()

    # mostrar el cuadro de diálogo y establecer la ventana principal
    messagebox.showinfo("Selecciona versión",
                        "Elige la versión que quieras, estas libre de mods para optimizar el rendimiento del juego en este caso", parent=root)

    # hacer que la ventana principal permanezca en primer plano
    root.lift()
    root.focus_force()

    # iniciar el bucle principal de la aplicación
    root.mainloop()

# función a ejecutar cuando se presiona el botón 2


def Mi_Survival():
    si_existe_carpeta()
    shutil.copytree(carpeta_Mi_Survival, Carpeta_Destino)
    ventana.destroy()
    minecraft_primer_plano()
    time.sleep(6)
    # Obtener las dimensiones de la pantalla
    width, height = pyautogui.size()
    # Hacer clic en la posición (x=100, y=100) de la pantalla
    pyautogui.click(x=951, y=805)
    time.sleep(1)
    pyautogui.scroll(-500)
    pyautogui.click(x=849, y=599)

# función a ejecutar cuando se presiona el botón 3


def Caballeros():
    si_existe_carpeta()
    shutil.copytree(carpeta_Caballeros, Carpeta_Destino)
    ventana.destroy()
    minecraft_primer_plano()
    # Abrimos la aplicación correspondiente al archivo2
    time.sleep(6)
    # Obtener las dimensiones de la pantalla
    width, height = pyautogui.size()
    # Hacer clic en la posición (x=100, y=100) de la pantalla
    pyautogui.click(x=951, y=805)
    time.sleep(1)
    pyautogui.click(x=837, y=781)

# función a ejecutar cuando se presiona el botón 4


def exit():
    ventana.destroy()
    tiempo_inicial = time.time()
    while (time.time() - tiempo_inicial) < 6:
        # ejecutar una serie de comandos aquí
        cerrar_minecraft()
        # esperar un breve periodo de tiempo antes de continuar
        time.sleep(0.1)


ventana = tk.Tk()
ventana.geometry("340x200")
ventana.config(bg="gold")
ventana.wm_attributes("-topmost", False)
ventana.overrideredirect(False)
ventana.geometry("+%d+%d" % (795, 354))

barra_titulo = tk.Frame(ventana, bg="blue", height=30)
barra_titulo.pack(fill="x")

espaciador_superior = tk.Frame(barra_titulo, bg="blue")
espaciador_superior.pack(side="top", fill="both", expand=True)

titulo = tk.Label(barra_titulo, text="Selecciona Servidor",
                  font=("Arial", 12), fg="red", bg="blue")
titulo.pack(padx=10, pady=10)

espaciador_inferior = tk.Frame(barra_titulo, bg="blue")
espaciador_inferior.pack(side="bottom", fill="both", expand=True)

contenido = tk.Label(ventana, text="Contenido de la ventana")
contenido.pack(padx=10, pady=10)

mi_fuente = ("Segoe_UI", 9)

boton1 = tk.Button(ventana, text="Vanilla", width=20, height=2,
                   cursor="hand2", font=mi_fuente, command=Vanilla)
boton2 = tk.Button(ventana, text="Mi Survival", width=20,
                   height=2, cursor="hand2", command=Mi_Survival)
boton3 = tk.Button(ventana, text="Caballeros", width=20,
                   height=2, cursor="hand2", font=mi_fuente, command=Caballeros)
boton4 = tk.Button(ventana, text="Exit", bg='red', width=20, height=2,
                   cursor="hand2", font=("Rextro", 9, "bold"), command=exit)

boton1.grid(row=2, column=0, pady=10, padx=10)
boton2.grid(row=2, column=1, pady=10, padx=10)
boton3.grid(row=3, column=0, pady=10, padx=10)
boton4.grid(row=3, column=1, pady=10, padx=10)

ventana.mainloop()
