import tkinter as tk
from tkinter import font

# Interfaz Gráfica Principal


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, 778, 406))


ventana = tk.Tk()
ventana.geometry("340x200")
ventana.config(bg="gold")
ventana.wm_attributes("-topmost", False)
ventana.overrideredirect(False)
center_window(ventana)

# Ajusta el tamaño del espaciador
barra_titulo = tk.Frame(ventana, bg="blue", height=10)
barra_titulo.pack(fill="x")

espaciador_superior = tk.Frame(barra_titulo, bg="blue")
espaciador_superior.pack(side="top", fill="both", expand=True)

titulo = tk.Label(barra_titulo, text="Ajuste de Mods",
                  font=("Adventure", 30, "bold"), fg="red", bg="blue")
titulo.pack(padx=0, pady=2)

espaciador_inferior = tk.Frame(barra_titulo, bg="blue")
espaciador_inferior.pack(side="bottom", fill="both", expand=True)

contenido = tk.Label(ventana, text="Elije el servidor:",
                     bg="gold", font=("Copperplate CC", 12, "bold"))
contenido.pack()

# Crear un contenedor para los botones en la columna izquierda
columna_izquierda = tk.Frame(ventana, bg="gold")
columna_izquierda.pack(side="left")

Fuente_Botones_Primarios = font.Font(weight="bold", size=9)

boton1 = tk.Button(columna_izquierda, bg="#C39CE6", fg="#DAFFA1", text="Vanilla", width=20, height=2,
                   cursor="hand2", font=Fuente_Botones_Primarios, command="")
boton2 = tk.Button(columna_izquierda, bg="#C39CE6", fg="#DAFFA1", text="Mi Survival", width=20,
                   height=2, cursor="hand2", font=Fuente_Botones_Primarios, command="")

boton1.pack(side="top", padx=10, pady=5)
boton2.pack(side="top", padx=10, pady=5)

# Crear un contenedor para los botones en la columna derecha
columna_derecha = tk.Frame(ventana, bg="gold")
columna_derecha.pack(side="left")

boton3 = tk.Button(columna_derecha, bg="#C39CE6", fg="#DAFFA1", text="Caballeros", width=20,
                   height=2, cursor="hand2", font=Fuente_Botones_Primarios, command="")

# Crear una fuente personalizada con negritas y un tamaño más grande
mi_fuente = font.Font(family="Copperplate Gothic", size=9, weight="bold")

boton4 = tk.Button(columna_derecha, text="Exit", bg='#BC0046', width=20,
                   height=2, cursor="hand2", fg="#00b41a", font=mi_fuente, command=exit)


boton3.pack(side="top", padx=10, pady=5)
boton4.pack(side="top", padx=10, pady=5)

ventana.mainloop()
# Interfaz Gráfica Principal
