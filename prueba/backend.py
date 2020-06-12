import eel

eel.init('web')

@eel.expose
def calculoICM(peso, altura):
    peso = float(peso)
    altura = float(altura)
    altura = altura**2
    altura = altura/1000
    datos = []
    imc = peso/(altura)
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
    

eel.start('index.html')