import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import time
import pyautogui

# 1
# Definimos las rutas predefinidas
ruta_predeterminada = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Verisones + mods"
ruta_predefinida = "C:/Users/osnir/AppData/Roaming/.minecraft"

# Creamos la ventana para seleccionar la carpeta
root = tk.Tk()
root.withdraw()

# Abrimos la ventana de diálogo para seleccionar la carpeta
initial_dir = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Verisones + mods"
ruta_carpeta = filedialog.askdirectory(initialdir=ruta_predeterminada, title='Seleccione la carpeta que desea mover')

# Obtenemos el nombre de la carpeta seleccionada
nombre_carpeta = os.path.basename(ruta_carpeta)

# Creamos la ruta completa de la carpeta de destino
ruta_destino = os.path.join(ruta_predefinida, nombre_carpeta)
# 1

# 2
# Si la carpeta de destino ya existe, la eliminamos
if os.path.exists("C:/Users/osnir/AppData/Roaming/.minecraft/mods"):
    shutil.rmtree("C:/Users/osnir/AppData/Roaming/.minecraft/mods")
# 2

# 3
# Copiamos la carpeta seleccionada a la carpeta de destino
if os.path.exists("C:/Users/osnir/AppData/Roaming/.minecraft/mods/vanilla"):
    messagebox.showinfo("Select the version", "Now you need to select the vanilla versión that you want, the predetermined versión is the las one on your launcher.")
    exit()
if not os.path.exists("C:/Users/osnir/AppData/Roaming/.minecraft/mods/vanilla"):
    shutil.copytree(ruta_carpeta, ruta_destino)

# Creamos la ventana emergente con el mensaje de confirmación
print(f"Se ha copiado la carpeta {nombre_carpeta} de la carpeta predeterminada a la carpeta predefinida.")
print("Cambio realizado con éxito")
# 3

time.sleep(1)
print("First part finished")
time.sleep(0.5)
print("Starting the second one")

# Definimos la ruta del directorio y la extensión de archivo deseada
ruta_directorio = f"{ruta_destino}"
extension_archivo = '.txt'

# Utilizamos la función os.listdir() para obtener el nombre de todos los archivos en el directorio
nombres_archivos = os.listdir(ruta_directorio)

# Creamos una lista con los nombres de los archivos que tienen la extensión deseada
archivos_con_extension = [archivo for archivo in nombres_archivos if archivo.endswith(extension_archivo)]

# Abre el minecarft
if not archivos_con_extension:
    messagebox.showerror(title='Error', message=f'No se encontraron archivos con la extensión {extension_archivo} en la ruta especificada.')
    exit()
else:
    subprocess.Popen("C:/Users/osnir/AppData/Roaming/.minecraft/TLauncher.exe")


# Si la lista de archivos con la extensión deseada está vacía, mostramos un mensaje de error
if not archivos_con_extension:
    messagebox.showerror(title='Error', message=f'No se encontraron archivos con la extensión {extension_archivo} en la ruta especificada.')
    exit()
else:
    # Recorremos la lista de archivos con la extensión deseada y abrimos la aplicación correspondiente
    for archivo in archivos_con_extension:
        if archivo.startswith('MiMundoSurvival'):
            time.sleep(6)
            # Obtener las dimensiones de la pantalla
            width, height = pyautogui.size()
            # Hacer clic en la posición (x=100, y=100) de la pantalla
            pyautogui.click(x=951, y=805)
            time.sleep(1)
            pyautogui.scroll(-500)
            pyautogui.click(x=849, y=599)
        elif archivo.startswith('Cavalleros'):
            # Abrimos la aplicación correspondiente al archivo2
            time.sleep(6)
            # Obtener las dimensiones de la pantalla
            width, height = pyautogui.size()
            # Hacer clic en la posición (x=100, y=100) de la pantalla
            pyautogui.click(x=951, y=805)
            time.sleep(1)
            pyautogui.click(x=837, y=781)
        elif archivo.startswith('Vanilla'):
            messagebox.showinfo("Elige la versión que quieras, estas libre de mods para optimizar el rendimiento del juego en este caso")
        else:
            # Si el nombre del archivo no coincide con ninguno de los anteriores, mostramos un mensaje de error
            messagebox.showerror(title='Error', message=f'No se encontró una aplicación correspondiente al archivo "{archivo}".')
            exit()

time.sleep(2)
messagebox.showinfo("All go well", "The process are all Okey, and the precess will continue execution...")
time.sleep(1)

# Crear una ventana de ejemplo
ventana = tk.Tk()
ventana.withdraw()

# Mostrar un cuadro de diálogo de información
messagebox.showinfo("Finish", "The task just finished.")


# Obtener las dimensiones de la pantalla
width, height = pyautogui.size()

# Hacer clic en la posición (x=100, y=100) de la pantalla
pyautogui.click(x=100, y=100)

