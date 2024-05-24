import tkinter as tk
from tkinter import messagebox


def error_message():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror(
        "Error 0xC0000135 ", message="Error 1: La ruta de acceso no existe o no coincide con ninguna ruta del sistema.")
    root.destroy()


error_message()
