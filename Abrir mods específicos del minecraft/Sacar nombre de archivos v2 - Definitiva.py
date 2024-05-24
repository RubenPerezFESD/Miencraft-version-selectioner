import os
import subprocess
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
    # Recorremos la lista de archivos con la extensión deseada y abrimos la aplicación correspondiente
    for archivo in archivos_con_extension:
        if archivo.startswith('notepad++'):
            # Abrimos la aplicación correspondiente al archivo1
            subprocess.Popen(["C:/Program Files/Notepad++/notepad++.exe", f'{ruta_directorio}/{archivo}'])
        elif archivo.startswith('VirtualBox'):
            # Abrimos la aplicación correspondiente al archivo2
            subprocess.Popen(["C:/Program Files/Oracle/VirtualBox/VirtualBox.exe", f'{ruta_directorio}/{archivo}'])
            # Abrimos la aplicación correspondiente al archivo3
        elif archivo.startswith('Revo Uninstaller'):
            subprocess.Popen(["C:/Program Files/VS Revo Group/Revo Uninstaller/RevoUnin.exe", f'{ruta_directorio}/{archivo}'])
        else:
            # Si el nombre del archivo no coincide con ninguno de los anteriores, mostramos un mensaje de error
            messagebox.showerror(title='Error', message=f'No se encontró una aplicación correspondiente al archivo {archivo}.')
