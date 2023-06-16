import tkinter as tk
from tkinter import font

ventana = tk.Tk()
ventana.geometry("340x200")
ventana.config(bg="gold")
ventana.wm_attributes("-topmost", True)
ventana.overrideredirect(False)
ventana.geometry("+%d+%d" % (795, 354))

# Ajusta el tamaño del espaciador
barra_titulo = tk.Frame(ventana, bg="blue", height=10)
barra_titulo.pack(fill="x")

espaciador_superior = tk.Frame(barra_titulo, bg="blue")
espaciador_superior.pack(side="top", fill="both", expand=True)

titulo = tk.Label(barra_titulo, text="Ajuste de Mods",
                  font=("Charmist DEMO", 24, "bold"), fg="red", bg="blue")
titulo.pack(padx=0, pady=0)  # Ajusta el tamaño del espaciado

espaciador_inferior = tk.Frame(barra_titulo, bg="blue")
espaciador_inferior.pack(side="bottom", fill="both", expand=True)

contenido = tk.Label(ventana, text="Contenido de la ventana",
                     bg="gold", font=("Arial", 12, "bold"))
contenido.pack(padx=0, pady=3)

# Crear un contenedor para los botones en la columna izquierda
columna_izquierda = tk.Frame(ventana, bg="gold")
columna_izquierda.pack(side="left")

boton1 = tk.Button(columna_izquierda, text="Vanilla", width=20, height=2,
                   cursor="hand2", command="")
boton2 = tk.Button(columna_izquierda, text="Mi Survival", width=20,
                   height=2, cursor="hand2")

boton1.pack(side="top", padx=10, pady=5)
boton2.pack(side="top", padx=10, pady=5)

# Crear un contenedor para los botones en la columna derecha
columna_derecha = tk.Frame(ventana, bg="gold")
columna_derecha.pack(side="left")

boton3 = tk.Button(columna_derecha, text="Caballeros", width=20,
                   height=2, cursor="hand2", command="")

# Crear una fuente personalizada con negritas y un tamaño más grande
mi_fuente = font.Font(family="Copperplate Gothic", size=9, weight="bold")

boton4 = tk.Button(columna_derecha, text="Exit", bg='#BC0046', width=20, height=2,
                   cursor="hand2", fg="green", font=mi_fuente, command=exit)

boton3.pack(side="top", padx=10, pady=5)
boton4.pack(side="top", padx=10, pady=5)

ventana.mainloop()
