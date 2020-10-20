"""
Calculadora de combinatoria simpre, compuesta y principio de multiplicación
Elaborado por:
Jean Pool Zambrano Hernandez
Jean Carlos Garzón Buitrago
"""

#Combinatoria-------------------------------------------------------------------------------------------------------------
def opcionUno(et, io, sr):
    if et.lower() == 'si' and io.lower() == 'si' and sr.lower() == 'no':
        print('Permutación')
        numberP = int(input('Digita el número:'))
        resultP = factorial(numberP)
        print('La permutación de: ' + str(numberP) + ' es ' + str(resultP))

    elif et.lower() == 'no' and io.lower() == 'si' and sr.lower() == 'no':
        print('Variación')
        numberUnoV = int(input('Digita el número mayor:'))
        numberDosV = int(input('Digita el número menor:'))
        restaV = numberUnoV - numberDosV
        resultDividendoV = factorial(numberUnoV)
        resultDivisorV = factorial(restaV)
        resultV = resultDividendoV / resultDivisorV
        print('La variación de ' + str(numberUnoV) + ' elementos tomados de ' + str(numberDosV) + ' es ' + str(resultV))

    elif et.lower() == 'si' and io.lower() == 'si' and sr.lower() == 'si':
        print('Permutación con Repetición')
        numberDividendoPR = int(input('Digita el número mayor:'))
        numero = int(input('Cuántos números desea ingresar para el divisor?'))
        numeroDivisor = multiplicacion(numero)
        resultDividendoPR = factorial(numberDividendoPR)   
        resultPR = resultDividendoPR / numeroDivisor
        print('La permutación con repetición de ' + str(numberDividendoPR) + ' elementos es ' + str(resultDividendoPR) + '/' + str(numeroDivisor) + ' = ' + str(resultPR))        

    elif et.lower() == 'no' and io.lower() == 'si' and sr.lower() == 'si':
        print('Variación con Repetición')
        numberUnoVR = int(input('Digita el número mayor:'))
        numberDosVR = int(input('Digita el número menor:'))
        resulVR = variacionRepetida(numberUnoVR, numberDosVR)
        print('La variación con repetición de ' + str(numberUnoVR) + ' elementos tomados de ' + str(numberDosVR) + ' es ' + str(resulVR))

    elif et.lower() == 'no' and io.lower() == 'no' and sr.lower() == 'si':
        print('Combinación con Repetición')
        numberUnoCR = int(input('Digita el número mayor:'))
        numberDosCR = int(input('Digita el número menor:'))
        sumaCR = (numberUnoCR + numberDosCR - 1)
        restaCR = numberUnoCR - 1
        resultDividendoCR = factorial(sumaCR)
        resultDivisorCRUno = factorial(numberDosCR) 
        resultDivisorCRDos = factorial(restaCR)
        resultCR = resultDividendoCR / (resultDivisorCRUno * resultDivisorCRDos)
        print('La combinación con repetición de ' + str(numberUnoCR) + ' elementos tomados de ' + str(numberDosCR) + ' es ' + str(resultCR))

    elif et.lower() == 'no' and io.lower() == 'no' and sr.lower() == 'no':
        print('Combinación')
        numberUnoC = int(input('Digita el número mayor:'))
        numberDosC = int(input('Difita el número menor:'))
        restaC = numberUnoC - numberDosC
        resultDividendoC = factorial(numberUnoC)
        resultDivisorCUno = factorial(restaC)
        resultDivisorCDos = factorial(numberDosC)
        resultC = resultDividendoC / (resultDivisorCUno *  resultDivisorCDos)
        print('La combinación de ' + str(numberUnoC) + ' elementos tomados de ' + str(numberDosC) + ' es ' + str(resultC))
    else:
        print('Error de combinación')

"""
Fórmula factorial
"""
def factorial(numberGeneral):
    if numberGeneral == 0:
        return 1

    return numberGeneral * factorial(numberGeneral - 1)  
"""
Fórmula Variación con Repetición
"""
def variacionRepetida(numberUnoVR, numberDosVR):
    return pow(numberUnoVR, numberDosVR)

"""
Fórmula Permutación con Repetición
"""
def multiplicacion(numero):
    ope = []
    for c in range(1, numero + 1):
        operator = int(input('Digita el número ' + str(c) + ':'))
        ope.append(factorial(operator))       
    return operacion(ope)
#--------------------------------------------------------------------------------------------------
#Principio de multiplicación
def opcionDos(dato):
    multi = []
    for c in range(1, dato + 1):
        multiplica = int(input('Digita el número ' + str(c) + ':'))
        multi.append(multiplica)
    print(multi)
    print(operacion(multi))

def operacion(lista):
    producto = 1
    for n in lista:
          producto *= n
    return producto 


if __name__ == "__main__":
    print("--------CALCULADORA DE COMBINATORIA SIMPLE, COMPUESTA Y PRINCIPIO DE MULTIPLICACIÓN-----------")
    print("----------------------------------------------------------------------------------------------")
    print('¿Qué desea hacer?')
    print('Combinatoria seleccione C')
    print('Principio de multiplicación seleccione P')

    eleccion = str(input('Su opción es: '))
    if eleccion.lower() == 'c':
        et = str(input('Entran todos? '))
        io = str(input('Importa el orden? '))
        sr = str(input('Se repiten? '))
        respuesta = opcionUno(et, io, sr)

    elif eleccion.lower() == 'p':
        dato = int(input('Cuantós números desea escribir?:'))
        respuesta2 = opcionDos(dato)
    