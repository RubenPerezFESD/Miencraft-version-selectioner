import os
import tkinter as tk
import tkinter
import shutil

window = tkinter.Tk()
window.title("Botones para mover carpetas")
window.geometry("300x200")

destination = "C:/Users/osnir/OneDrive/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/destination"
path2 = "C:/Users/osnir/OneDrive/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/destination/Origen/path2"
path3 = "C:/Users/osnir/OneDrive/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/destination/Origen/path3"
path4 = "C:/Users/osnir/OneDrive/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/destination/Origen/path4"
path5 = "C:/Users/osnir/OneDrive/Miencraft version selectioner/Envio de pruebas (carpeta=mods)/destination/Origen/path5"


def delete():
    for file in os.listdir(destination):
        if file.endswith('.jar') and os.path.isfile(os.path.join(destination, file)):
            os.remove(os.path.join(destination, file))


def copy_files(source, destination):
    for root, directories, files in os.walk(source):
        for file in files:
            if file.endswith('.jar'):
                shutil.copy(os.path.join(root, file), destination)


def mover1():
    delete()
    "Moves the folder in path1 to path2"
    copy_files(path2, destination)


def mover2():
    delete()
    "Moves the folder in path3 to path2"
    copy_files(path3, destination)


def mover3():
    delete()
    "Moves the folder in path4 to path2"
    copy_files(path4, destination)


def mover4():
    delete()
    "Moves the folder in path5 to path2"
    copy_files(path5, destination)


boton1 = tk.Button(text="Mover 1", command=mover1)
boton1.pack()

boton2 = tk.Button(text="Mover 2", command=mover2)
boton2.pack()

boton3 = tk.Button(text="Mover 3", command=mover3)
boton3.pack()

boton4 = tk.Button(text="Mover 4", command=mover4)
boton4.pack()

boton5 = tk.Button(text="prueba", command=delete)
boton5.pack()

window.mainloop()
