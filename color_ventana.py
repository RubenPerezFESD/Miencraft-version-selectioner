import tkinter as tk

ventana = tk.Tk()
ventana.overrideredirect(True)  # Elimina la barra de título predeterminada

# Diseño de la barra de título personalizada
barra_titulo = tk.Frame(ventana, bg="blue", height=30)
barra_titulo.pack(fill="x")

ventana.wm_attributes("-topmost", True)

titulo = tk.Label(barra_titulo, text="Mi Ventana", fg="white",
                  font=("Arial", 14, "bold"), bg="blue")
titulo.pack(padx=10, pady=5)

# Contenido de la ventana
contenido = tk.Label(ventana, text="Contenido de la ventana")
contenido.pack()

ventana.mainloop()
