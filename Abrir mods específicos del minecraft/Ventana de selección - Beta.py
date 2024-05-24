import tkinter as tk

# Funcion para el movimiento de la carpeta


def mover_carpeta():
    print("Carpeta movida")

# Funcion a ejecutar cuando se preisone el boton correspondiente


def funcion_boton1():
    print("Se presionó el botón 1")


def funcion_boton2():
    print("Se presionó el botón 2")


def funcion_boton3():
    print("Se presionó el botón 3")


def funcion_boton4():
    print("Se presionó el botón 4")


# Crear la ventana y definir sus dimensiones
ventana = tk.Tk()
ventana.geometry("340x200")

# Hacer que la ventana no se pueda mover
ventana.overrideredirect(False)

# Establecer la posición de la ventana en el centro de la pantalla
ventana.geometry("+%d+%d" % (795, 354))

# Crear un widget Label con el título en la parte central superior
titulo = tk.Label(ventana, text="Selecciona Servidor", font=("Arial", 24))
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Crear los botones
boton1 = tk.Button(ventana, text="Vanilla", width=20,
                   height=2, command=funcion_boton1)
boton2 = tk.Button(ventana, text="Mi Survival", width=20,
                   height=2, command=funcion_boton2)
boton3 = tk.Button(ventana, text="Caballeros", width=20,
                   height=2, command=funcion_boton3)
boton4 = tk.Button(ventana, text="Botón 4", width=20,
                   height=2, command=funcion_boton4)

# Colocar los botones utilizando grid()
boton1.grid(row=1, column=0, pady=10, padx=10)
boton2.grid(row=1, column=1, pady=10, padx=10)
boton3.grid(row=2, column=0, pady=10, padx=10)
boton4.grid(row=2, column=1, pady=10, padx=10)

# Mantener la ventana abierta
ventana.mainloop()
