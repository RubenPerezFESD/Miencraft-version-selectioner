import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import filedialog, messagebox

# Definimos las rutas predefinidas
ruta_predeterminada = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Origen"
ruta_predefinida = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Destino"

# Creamos la ventana para seleccionar la carpeta
root = tk.Tk()
root.withdraw()

# Abrimos la ventana de diálogo para seleccionar la carpeta
ruta_carpeta = filedialog.askdirectory(initialdir=ruta_predeterminada, title='Seleccione la carpeta que desea mover')

# Obtenemos el nombre de la carpeta seleccionada
nombre_carpeta = os.path.basename(ruta_carpeta)

# Creamos la ruta completa de la carpeta de destino
ruta_destino = os.path.join(ruta_predefinida, nombre_carpeta)

# Si la carpeta de destino ya existe, la eliminamos
if os.path.exists(ruta_destino):
    shutil.rmtree(ruta_destino)

# Copiamos la carpeta seleccionada a la carpeta de destino
shutil.copytree(ruta_carpeta, ruta_destino)

# Creamos la ventana emergente con el mensaje de confirmación
mensaje_confirmacion = f'Se ha copiado la carpeta {nombre_carpeta} de la carpeta predeterminada a la carpeta predefinida.'
messagebox.showinfo(title='Cambio realizado con éxito', message=mensaje_confirmacion)