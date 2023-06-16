import tkinter as tk
from tkinter import messagebox
import shutil
import os
import subprocess
import signal
import time


carpeta_Mi_Survival = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/Servidores/Mi Survival"
carpeta_Caballeros = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/Servidores/Caballeros"
Carpeta_Destino = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/mods"


def si_existe_carpeta():
    # Si la carpeta de destino ya existe, borramos su contenido
    if os.path.exists(Carpeta_Destino):
        shutil.rmtree(Carpeta_Destino)


def cerrar_minecraft():
    # iniciar el proceso del programa
    proceso = subprocess.Popen("javaw.exe")
    # obtener el ID del proceso
    pid = proceso.pid
    # cerrar el programa
    os.kill(pid, signal.SIGTERM)


def Vanilla():
    si_existe_carpeta()
    ventana.destroy()
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


def Mi_Survival():
    si_existe_carpeta()
    shutil.copytree(carpeta_Mi_Survival, Carpeta_Destino)
    ventana.destroy()


def Caballeros():
    si_existe_carpeta()
    shutil.copytree(carpeta_Caballeros, Carpeta_Destino)
    ventana.destroy()


def exit():
    ventana.destroy()
    tiempo_inicial = time.time()
    while (time.time() - tiempo_inicial) < 6:
        # ejecutar una serie de comandos aquí
        cerrar_minecraft()
        # esperar un breve periodo de tiempo antes de continuar
        time.sleep(0.1)


# Crear la ventana y definir sus dimensiones
ventana = tk.Tk()
ventana.geometry("340x200")

# configurar la ventana para que se mantenga en primer plano
ventana.wm_attributes("-topmost", True)

# Hacer que la ventana no se pueda mover
ventana.overrideredirect(False)

# Establecer la posición de la ventana en el centro de la pantalla
ventana.geometry("+%d+%d" % (795, 354))

# Crear un widget Label con el título en la parte central superior
titulo = tk.Label(ventana, text="Selecciona Servidor", font=("Arial", 24))
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Crear los botoness
boton1 = tk.Button(ventana, text="Vanilla", width=20,
                   height=2, command=Vanilla)
boton2 = tk.Button(ventana, text="Mi Survival", width=20,
                   height=2, command=Mi_Survival)
boton3 = tk.Button(ventana, text="Caballeros", width=20,
                   height=2, command=Caballeros)
boton4 = tk.Button(ventana, text="Exit", bg='red', width=20,
                   height=2, command=exit)

# Colocar los botones utilizando grid()
boton1.grid(row=1, column=0, pady=10, padx=10)
boton2.grid(row=1, column=1, pady=10, padx=10)
boton3.grid(row=2, column=0, pady=10, padx=10)
boton4.grid(row=2, column=1, pady=10, padx=10)

# Mantener la ventana abierta
ventana.mainloop()
