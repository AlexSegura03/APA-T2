## FUNCION ES PRIMO

"""
Àlex Segura Medina


>>> esPrimo(5)
True

>>> esPrimo(2)
True

>>> esPrimo(74211)
False
"""

def esPrimo(numero):
    """
    Devuelve True si el número es primo y False si no lo es.

    >>> for numero in range(2, 10): 
    ...     print(esPrimo(numero))
    True
    True
    False
    True
    False
    True
    False
    False
    """
    for prova in range(2, numero):
        if numero % prova == 0:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
## ----------------------------------------------------------------------

## FUNCIÓN PRIMOS

"""
Àlex Segura Medina

>>> primos(10)
(2, 3, 5, 7)

>>> primos(17)
(2, 3, 5, 7, 11, 13)

>>> primos(45)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)

"""

def primos(numero):
    """

    Devuelve una tupla con todos los números primos menores que su argumento."

    >>> lista = []
    >>> for numero in range(2, 20):
    ...     if esPrimo(numero):
    ...     lista.append(numero)
    ... return tuple(lista)

   (2, 3, 5, 7, 11, 13, 17, 19)
    
    """
    lista = []
    for i in range(2, numero):
        if esPrimo(i):
            lista.append(i)
    return tuple(lista)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


## ----------------------------------------------------------------------

## FUNCIÓN DESCOMPONER PRIMOS

""""
Àlex Segura Medina

>>> descompon()

"""

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.

    >>> descompon(12)
    2, 2, 3
   
    >>> descompon(45)
    3, 3, 5

    >>> descompon(72)
    2, 2, 2, 3, 3

    """
    factores = []
    divisor = 2
    
    def descompon(numero):
        factores = []
        divisor = 2
            while numero > 1:
                while numero % divisor == 0:
                    factores.append(divisor)
                    numero //= divisor
                divisor += 1
        return tuple(factores)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


