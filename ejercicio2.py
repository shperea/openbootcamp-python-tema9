# En este segundo ejercicio, teneis que crear una aplicacion que obtendra los elementos impares de
# una lista pasada por parametro con filter y realizara una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

def lista_numeros(valor_inicial, valor_final):
    """
    Forma un rango de valores a partir de dos numeros.
    El ultimo numero esta incluido en el rango.

    """
    if valor_inicial > valor_final:
        return [*range(valor_inicial, valor_final - 1, -1)]
    else:
        return [*range(valor_inicial, valor_final + 1, 1)]

numeros = lista_numeros(int(input("Valor inicial: ")), int(input("Valor final: ")))

impares = list(filter(lambda x: x % 2 != 0, numeros))  # Filtra los numeros impares

resultado_suma = reduce(lambda x, y: x + y, impares)  # Suma todos los numeros

print(f'Resultado: {resultado_suma}')