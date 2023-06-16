import shutil
import os

Mi_Survival = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/Servidores/Mi Survival"
Carpeta_Destino = "C:/Users/osnir/OneDrive/Documentos/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/mods"


def si_existe_carpeta():
    # Si la carpeta de destino ya existe, borramos su contenido
    if os.path.exists(Carpeta_Destino):
        shutil.rmtree(Carpeta_Destino)


def Mi_Survival():
    si_existe_carpeta()
    shutil.copytree(Mi_Survival, Carpeta_Destino)


Mi_Survival()
