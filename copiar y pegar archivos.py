import shutil
import os

# Carpeta de origen (donde se copiarán los archivos)
carpeta_origen = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/.Origen"

# Carpeta de destino (donde se pegarán los archivos)
carpeta_destino = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/.Destino"


# Extensión de archivo a eliminar (por ejemplo, ".txt")
extension_a_eliminar = ".txt"

# Obtener la lista de archivos en la carpeta de destino
archivos_destino = os.listdir(carpeta_destino)

# Eliminar los archivos con la extensión especificada en la carpeta de destino
for archivo_destino in archivos_destino:
    ruta_archivo_destino = os.path.join(carpeta_destino, archivo_destino)
    if os.path.isfile(ruta_archivo_destino) and archivo_destino.endswith(extension_a_eliminar):
        os.remove(ruta_archivo_destino)

# Obtener la lista de archivos en la carpeta de origen
archivos_origen = os.listdir(carpeta_origen)

# Copiar cada archivo a la carpeta de destino
for archivo_origen in archivos_origen:
    ruta_origen = os.path.join(carpeta_origen, archivo_origen)
    ruta_destino = os.path.join(carpeta_destino, archivo_origen)
    shutil.copy2(ruta_origen, ruta_destino)

print("Archivos copiados exitosamente.")
