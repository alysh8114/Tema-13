"""Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función
recibe como parámetros los valores de dos de sus lados. En el bloque principal del programa
cargar los lados de dos rectángulos y luego mostrar cuál de los dos tiene una superficie mayor."""

def superficie_rectanfulo1(lado1, lado2):
    rectangulo = lado1 * lado2
    return rectangulo
print("PRIMER RECTANGULO")
lado1 = int(input("Ingresar el lado del rectangulo: "))
lado2 = int(input("Ingresar el ancho del rectangulo: "))
print("La superficie del rectangulo es", superficie_rectanfulo1(lado1, lado2))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def superficie_rectanfulo2(lado3, lado4):
    rectangulo = lado3 * lado4
    return rectangulo
print("SEGUNDO RECTANGULO")
lado3 = int(input("Ingrese el largo del rectangulo: "))
lado4 = int(input("Ingrese el ancho del rectangulo: "))
print("La superficie del rectangulo es", superficie_rectanfulo2(lado3, lado4))

if superficie_rectanfulo1(lado1, lado2) > superficie_rectanfulo2(lado3, lado4):
    print("El PRIMER RECTANGULO tiene una superficie mayor")
else:
    print("El SEGUNDO RECTANGULO tiene una superficie mayor")
if superficie_rectanfulo1(lado1, lado2) == superficie_rectanfulo2(lado3, lado4):
    print("La superficie del PRIMER RECTANGULO y el SEGUNDO RECTANGULO son iguales")

