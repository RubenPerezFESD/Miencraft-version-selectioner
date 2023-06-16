import pygetwindow as gw
import time

time.sleep(3)

# Obtener la ventana actual
ventana_actual = gw.getActiveWindow()

# Obtener la posición actual de la ventana
x, y = ventana_actual.topleft

print("La posición actual de la ventana es: ({}, {})".format(x, y))

input()
