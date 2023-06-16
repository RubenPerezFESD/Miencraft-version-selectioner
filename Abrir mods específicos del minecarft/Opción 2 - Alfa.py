from tkinter import *
from tkinter import ttk
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import time

# Definimos las rutas predefinidas
ruta_predeterminada = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Origen"
ruta_predefinida = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Destino"

# Creamos la ventana para seleccionar la carpeta
root = tk.Tk()
root.withdraw()

# Abrimos la ventana de diálogo para seleccionar la carpeta
initial_dir = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Origen"

def obtener_info():
    #OBTENER ELEMENTO SELECCIONADO
    print(lista_desplegable.get())

ventana = Tk()
ventana.title("Lista Desplegable")
ventana.geometry('300x190')

# LISTA DESPLEGABLE.
lista_desplegable = ttk.Combobox(ventana,width=17)
lista_desplegable.place(x=30, y=77)
# LISTA DESPLEGABLE.
lista_desplegable = ttk.Combobox(ventana,width=17, state='readonly' )
lista_desplegable.place(x=30,y=77)

Notepad = "C:/Program Files/Notepad++/notepad++.exe"
VirtualBox = "C:/Program Files/Oracle/VirtualBox/VirtualBox.exe"
RevoUnistaller = "C:/Program Files/VS Revo Group/Revo Uninstaller/RevoUnin.exe"

#LISTA DE OPCIONES.
opciones = ["Notepad++","VirtualBox","RevoUnistaller"]

#INSERTAR VALORES.
lista_desplegable['values']=opciones
#BOTON ‘obtener’.
Button(ventana, text="obtener",bg="gold",command=obtener_info).place(x=170, y=77)

ventana.mainloop()

# Obtenemos el nombre de la carpeta seleccionada
nombre_carpeta = os.path.basename(obtener_info)

# Creamos la ruta completa de la carpeta de destino
ruta_destino = os.path.join(ruta_predefinida, nombre_carpeta)

# Si la carpeta de destino ya existe, la eliminamos
if os.path.exists(ruta_destino):
    shutil.rmtree(ruta_destino)

# Copiamos la carpeta seleccionada a la carpeta de destino
shutil.copytree(obtener_info, ruta_destino)

# Creamos la ventana emergente con el mensaje de confirmación
print(f"Se ha copiado la carpeta {nombre_carpeta} de la carpeta predeterminada a la carpeta predefinida.")
print("Cambio realizado con éxito")

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

# Si la lista de archivos con la extensión deseada está vacía, mostramos un mensaje de error
if not archivos_con_extension:
    messagebox.showerror(title='Error', message=f'No se encontraron archivos con la extensión {extension_archivo} en la ruta especificada.')
else:
    # Recorremos la lista de archivos con la extensión deseada y abrimos la aplicación correspondiente
    for archivo in archivos_con_extension:
        if archivo.startswith('Notepad++'):
            # Abrimos la aplicación correspondiente al archivo1
            subprocess.Popen(["C:/Program Files/Notepad++/notepad++.exe", f'{ruta_directorio}/{archivo}'])
        elif archivo.startswith('VirtualBox'):
            # Abrimos la aplicación correspondiente al archivo2
            subprocess.Popen(["C:/Program Files/Oracle/VirtualBox/VirtualBox.exe", f'{ruta_directorio}/{archivo}'])
            # Abrimos la aplicación correspondiente al archivo3
        elif archivo.startswith('RevoUnistaller'):
            subprocess.Popen(["C:/Program Files/VS Revo Group/Revo Uninstaller/RevoUnin.exe", f'{ruta_directorio}/{archivo}'])
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
