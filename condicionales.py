#condicionales
'''
a =8
b = 10
c = 13

if a<=c:
    if b<c:
        print("5 no es menor a 4")
    else:
        print("No se cumpel la condicion")
'''

#imc calculadora
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Tu IMC es", imc, "y estás por debajo del peso saludable.")
elif imc >= 18.5 and imc < 25:
    print("Tu IMC es", imc, "y estás en un rango de peso saludable.")
elif imc >= 25 and imc < 30:
    print("Tu IMC es", imc, "y estás en sobrepeso.")
elif imc >= 30 and imc < 35:
    print("Tu IMC es", imc, "y estás en un rango de obesidad I")
elif imc >= 35 and imc < 40:
    print("Tu IMC es", imc, "y estás en un rango de obesidad II")
elif imc >= 40 and imc < 50:
    print("Tu IMC es", imc, "y estás en un rango de obesidad III")
else:
    print("Tu IMC es", imc, "y estás en un rango de obesidad IV")

