
"""
Àlex Segura Medina

TESTS UNITARIOS:
>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)
>>> mcm(90, 14)
630
>>> mcd(924, 780)
12
>>> mcmN(42, 60, 70, 63)
1260
>>> mcdN(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """
    Devuelve True si el número es primo y False si no lo es.
    """
    for prova in range(2, numero):
        if numero % prova == 0:
            return False
    return True

    
## ----------------------------------------------------------------------

## FUNCIÓN PRIMOS

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento."
    """
    lista = []
    for i in range(2, numero):
        if esPrimo(i):
            lista.append(i)
    return tuple(lista)

## ----------------------------------------------------------------------

## FUNCIÓN DESCOMPONER PRIMOS

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    """
    
    factores = []
    if numero < 2:
        return tuple()
    
    # Manejo especial para números negativos
    if numero < 0:
        factores.append(-1)
        numero = -numero
    
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero = numero // divisor
        divisor += 1
        if divisor * divisor > numero and numero > 1:
            factores.append(numero)
            break
    return tuple(factores)

## ----------------------------------------------------------------------

## FUNCIÓN MCM

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de dos números.
    """
    descomposicion1 = descompon(numero1)
    descomposicion2 = descompon(numero2)
    
    factores_mcm = {}
    
    for factor in descomposicion1:
        factores_mcm[factor] = factores_mcm.get(factor, 0) + 1
    
    for factor in descomposicion2:
        if factores_mcm.get(factor, 0) < descomposicion2.count(factor):
            factores_mcm[factor] = descomposicion2.count(factor)
    
    mcm = 1
    for factor, exponente in factores_mcm.items():
        mcm *= factor ** exponente
    
    return mcm

## ----------------------------------------------------------------------

## FUNCIÓN MCD


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    
    # Creamos un diccionario con los factores mínimos comunes
    factores_mcd = {}
    
    for factor in set(factores1):
        if factor in factores2:
            min_count = min(factores1.count(factor), factores2.count(factor))
            factores_mcd[factor] = min_count
    
    resultado = 1
    for factor, exponente in factores_mcd.items():
        resultado *= factor ** exponente
    
    return resultado

## ----------------------------------------------------------------------

## FUNCIÓN MCM CON NÚMEROS ARBITRARIOS

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.    
    """
    if not numeros:
        return 0
    
    # Inicializamos con el primer número
    current_mcm = numeros[0]
    
    for num in numeros[1:]:
        current_mcm = mcm(current_mcm, num)
    
    return current_mcm


## ----------------------------------------------------------------------

## FUNCIÓN MCD CON NÚMEROS ARBITRARIOS

def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    if not numeros:
        return 0
    
    # Inicializamos con el primer número
    current_mcd = numeros[0]
    
    for num in numeros[1:]:
        current_mcd = mcd(current_mcd, num)
    
    return current_mcd


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
