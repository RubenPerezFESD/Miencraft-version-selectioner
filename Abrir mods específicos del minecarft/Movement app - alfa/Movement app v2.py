import shutil
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Definir la ruta predefinida de la carpeta origen y destino
ruta_origen = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Origen"
ruta_destino = "C:/Users/osnir/OneDrive/Documentos/Nueva_carpeta/Destino"

# Crear una ventana para seleccionar la carpeta
Tk().withdraw() 
ruta_carpeta = askdirectory(title="Seleccionar carpeta a mover")

# Obtener el nombre de la carpeta que el usuario desea copiar
nombre_carpeta = os.path.basename(ruta_carpeta)

# Comprobar para eliminar carpeta con el mismo nombre en el destino
if os.path.exists(os.path.join(ruta_destino, nombre_carpeta)):
    shutil.rmtree(ruta_destino, nombre_carpeta)

else:
    # Crear una copia de la carpeta en la ruta destino
    shutil.copytree(os.path.join(ruta_origen, nombre_carpeta), os.path.join(ruta_destino, nombre_carpeta))

    # Confirmar que la carpeta ha sido copiada
    if os.path.exists(os.path.join(ruta_destino, nombre_carpeta)):
        print("Carpeta copiada con éxito.")

    else:
        print("Ha ocurrido un error al copiar la carpeta.")
