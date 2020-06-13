import os
import sys
import platform
import eel
import math

eel.init('web')

@eel.expose
def calculoICM(peso, altura):
    peso = float(peso)
    altura = float(altura)
    altura = altura**2
    altura = altura/10000
    datos = []
    imc = peso/(altura)
    imc = round(imc, 2)
    datos.append((imc))

    if(imc <= 18.5):
        datos.append("Peso inferior al normal")
    elif(imc <= 24.9):
        datos.append("Peso normal")
    elif(imc < 29.9):
        datos.append("Peso superior al normal")
    else:
        datos.append("Obesidad")
    
    return datos
    
#Launching Edge can also be gracefully handled as a fall back
try:
    eel.start('index.html', mode='chrome', size=(1000, 600))
except EnvironmentError:
    # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        eel.start('index.html', mode='edge')
    else:
        raise