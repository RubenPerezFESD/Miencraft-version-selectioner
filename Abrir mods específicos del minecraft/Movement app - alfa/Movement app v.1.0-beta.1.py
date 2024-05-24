import shutil
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

ruta_origen = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Origen"
ruta_destino = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Destino"

# Crear una ventana para seleccionar la carpeta
Tk().withdraw()
ruta_carpeta = askdirectory(title="Seleccionar carpeta a mover")

nombre_carpeta = os.path.basename(ruta_carpeta)

# Mover la carpeta a la nueva ubicación
shutil.move(os.path.join(ruta_origen, nombre_carpeta), os.path.join(ruta_destino, nombre_carpeta))

# Eliminar la carpeta de la ruta predefinida
shutil.rmtree(os.path.join(ruta_origen, nombre_carpeta))
