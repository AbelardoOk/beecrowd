# -*- coding: utf-8 -*-

a = float(input().replace(',', '.'))
b = float(input().replace(',', '.'))
c = float(input().replace(',', '.'))

areaTriangle = (a*c) / 2
areaCircle = c**2 * 3.14159
areaTrapeze = ((a + b) * c) / 2
areaSquare = b**2
areaRetangle = a * b

print("TRIANGULO: {:.3f} \nCIRCULO: {:.3f} \nTRAPEZIO: {:.3f} \nQUADRADO: {:.3f} \nRETANGULO: {:.3f}".format(areaTriangle, areaCircle, areaTrapeze, areaSquare, areaRetangle))