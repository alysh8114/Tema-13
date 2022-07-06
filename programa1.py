"""Elaborar una función que nos retorne el perímetro de un cuadrado
pasando como parámetros el valor de un lado."""

def retornar_perimetro(lado):
    perimetro = lado+lado+lado+lado
    return perimetro

valor=int(input("Ingrese el valor de un lado del cuadrado: "))
perimetro = retornar_perimetro(valor)
print("El perimetro del cuadrado es:",perimetro)

