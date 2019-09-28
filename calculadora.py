# Ejercicio de calculadora para Kata simple
# la calculadora procesa un string en el que
# vienen 0, 1 o 2 números separados por coma
# si vienen 2 números devuelve la suma de ellos
# si viene solo un número devuelve ese número
# si el string es vacío devuelve 0


class Calculadora:
    def suma(cadena):
        if cadena == "":
            return 0
        elif ',' in cadena:
            nums = cadena.split(",")
            suma = 0
            for n in nums:
                suma += int(n)

            return suma
        else:
            return int(cadena)
