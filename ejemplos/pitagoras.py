from decimal import Decimal
from numpy import sqrt

a = Decimal(input('Dime la medida de uno de los catetos: '))
b = Decimal(input('Dime la medida del otro: '))

c = sqrt(a ** 2 + b ** 2)

print(c)
