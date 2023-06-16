import os
import tkinter as tk
from tkinter import messagebox

# Definimos la ruta del directorio y la extensión de archivo deseada
ruta_directorio = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Origen/1"
extension_archivo = '.txt'

# Utilizamos la función os.listdir() para obtener el nombre de todos los archivos en el directorio
nombres_archivos = os.listdir(ruta_directorio)

# Creamos una lista con los nombres de los archivos que tienen la extensión deseada
archivos_con_extension = [archivo for archivo in nombres_archivos if archivo.endswith(extension_archivo)]

# Si la lista de archivos con la extensión deseada está vacía, mostramos un mensaje de error
if not archivos_con_extension:
    messagebox.showerror(title='Error', message=f'No se encontraron archivos con la extensión {extension_archivo} en la ruta especificada.')
else:
    # Creamos una cadena de texto con los nombres de los archivos separados por saltos de línea
    nombres_archivos_con_extension = '\n'.join(archivos_con_extension)
    
    # Creamos una ventana emergente con los nombres de los archivos
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title='Archivos con extensión especificada', message=nombres_archivos_con_extension)