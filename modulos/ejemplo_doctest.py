def sumar(a: int, b: int) -> int:
    '''
    Suma dos números a y b.
    
    >>> print(sumar(2, 3))
    5
    '''
    return a + b

print(sumar(10, 5))

import doctest
doctest.testmod()
