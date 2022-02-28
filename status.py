import psutil
import os

while True:
    procesos = 0
    for proc in psutil.process_iter():

        if proc.name().lower() == 'main.exe' or proc.name().lower() == 'python.exe':
            procesos += 1
        
    if procesos == 1:
        # todo: ejecutar la app si esta caida
        print('La aplicación se cerró de forma inesperada. Abriendo...')
        os.system('python main.py')
    
    else:
        print('La aplicación principal se esta ejecutando correctamente')