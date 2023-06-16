import subprocess
import os
import signal
import time

# iniciar el proceso del programa
proceso = subprocess.Popen("notepad.exe")

# obtener el ID del proceso
pid = proceso.pid

# esperar 5 segundos antes de cerrar el programa
time.sleep(5)

# cerrar el programa utilizando la señal SIGKILL
os.kill(pid, signal.CTRL_C_EVENT)
