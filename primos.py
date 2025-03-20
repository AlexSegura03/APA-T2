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
    