import tkinter as tk
from tkinter import messagebox
from tkinter import font
import shutil
import os
import sys
import subprocess
import time

# Rutas de las carpetas
destination = "C:/Users/osnir/AppData/Roaming/.minecraft/mods"                   # Carpeta de mods
mi_survival = "C:/Users/osnir/AppData/Roaming/.minecraft/mods/Mi Mundo"          # Caballeros
caballeros = "C:/Users/osnir/AppData/Roaming/.minecraft/mods/Caballeros"         # Mi Mundo
vanilla = ""                                                                     # - - -
path4 = ""                                                                       # - - -

# Abrir Minecraft
subprocess.run("C:/Users/osnir/AppData/Roaming/.minecraft/TLauncher.exe")

# eliminador de archivos .jar existentes e inecesarios


def delete():
    for file in os.listdir(destination):
        if file.endswith('.jar') and os.path.isfile(os.path.join(destination, file)):
            os.remove(os.path.join(destination, file))

# función del copia y pega


def copy_files(source, destination):
    for root, directories, files in os.walk(source):
        for file in files:
            if file.endswith('.jar'):
                shutil.copy(os.path.join(root, file), destination)

# función del mensaje de error


def error_message():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror(
        "Error 0xC0000135 ", message="Error 1: La ruta de acceso no existe o no coincide con ninguna ruta del sistema.")
    root.destroy()


# Funciones definadas a cada botón
def mover1():  # mi_survival
    if not os.path.exists(destination):
        error_message()
        time.sleep(.5)
        sys.exit()
    if not os.path.exists(mi_survival):
        error_message()
        time.sleep(.5)
        sys.exit()
    else:
        delete()
        copy_files(mi_survival, destination)
        sys.exit()


def mover2():  # Caballeros
    if not os.path.exists(destination):
        error_message()
        time.sleep(.5)
        sys.exit()
    if not os.path.exists(caballeros):
        error_message()
        time.sleep(.5)
        sys.exit()
    else:
        delete()
        copy_files(caballeros, destination)
        sys.exit()


def mover3():  # Vanilla
    delete()
    sys.exit()


def mover4(): # - - -
    if not os.path.exists(destination):
        error_message()
        time.sleep(.5)
        sys.exit()
    if not os.path.exists(path4):
        error_message()
        time.sleep(.5)
        sys.exit()
    else:
        delete()
        copy_files(path4, destination)
        sys.exit()

# Interfaz Gráfica Principal


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, 778, 406))


ventana = tk.Tk()
ventana.geometry("340x200")
ventana.resizable(0, 0)
ventana.config(bg="gold")
ventana.wm_attributes("-topmost", True)
ventana.overrideredirect(False)
ventana.title("Intercambiadora de mods")
center_window(ventana)

# Ajusta el tamaño del espaciado
barra_titulo = tk.Frame(ventana, bg="blue", height=10)
barra_titulo.pack(fill="x")

espaciador_superior = tk.Frame(barra_titulo, bg="blue")
espaciador_superior.pack(side="top", fill="both", expand=True)

titulo = tk.Label(barra_titulo, text="Ajuste de Mods",
                  font=("Adventure", 30, "bold"), fg="red", bg="blue")
titulo.pack(padx=0, pady=2)

espaciador_inferior = tk.Frame(barra_titulo, bg="blue")
espaciador_inferior.pack(side="bottom", fill="both", expand=True)

contenido = tk.Label(ventana, text="Elije el servidor:",
                     bg="gold", font=("Copperplate CC", 12, "bold"))
contenido.pack()

# Crear un contenedor para los botones en la columna izquierda
columna_izquierda = tk.Frame(ventana, bg="gold")
columna_izquierda.pack(side="left")

Fuente_Botones_Primarios = font.Font(weight="bold", size=9)

# Botones 1 & 3
boton1 = tk.Button(columna_izquierda, bg="#C39CE6", fg="#DAFFA1", text="Mi Survival", width=20, height=2,
                   cursor="hand2", font=Fuente_Botones_Primarios, command=mover1)
boton2 = tk.Button(columna_izquierda, bg="#C39CE6", fg="#DAFFA1", text="Vanilla", width=20,
                   height=2, cursor="hand2", font=Fuente_Botones_Primarios, command=mover3)

boton1.pack(side="top", padx=10, pady=5)
boton2.pack(side="top", padx=10, pady=5)

# Crear un contenedor para los botones en la columna derecha
columna_derecha = tk.Frame(ventana, bg="gold")
columna_derecha.pack(side="left")

# Crear una fuente personalizada con negritas y un tamaño más grande
mi_fuente = font.Font(family="Copperplate Gothic", size=9, weight="bold")

# Botones 2 & 4s
boton3 = tk.Button(columna_derecha, bg="#C39CE6", fg="#DAFFA1", text="Caballeros", width=20,
                   height=2, cursor="hand2", font=Fuente_Botones_Primarios, command=mover2)
boton4 = tk.Button(columna_derecha, text="Exit", bg='#BC0046', width=20,
                   height=2, cursor="hand2", fg="#00b41a", font=mi_fuente, command=sys.exit)

boton3.pack(side="top", padx=10, pady=5)
boton4.pack(side="top", padx=10, pady=5)

ventana.mainloop()
