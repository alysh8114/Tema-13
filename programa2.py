"""Plantear una función que reciba un string en mayúsculas o minúsculas
y retorne la cantidad de letras “a” o “A”. """

def cantidad_de_a(palabra):
    cantidad = 0
    for i in range(len(palabra)):
        if (palabra[i] == "a") or (palabra[i] == "A"):
            cantidad += 1
    return cantidad
palabras=input("Ingresar una palabra: ")
print("La palabra",palabras, "tiene",cantidad_de_a(palabras), "letras a")