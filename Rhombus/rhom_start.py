#Rhombus
from Rhombus import perimeter, area


def operation():
    op = int(input('[1] Area\n'
                   '[2] Perimeter\n'))
    if op == 1:
        print('The area is: ', area.calc())
    elif op == 2:
        print('The perimeter', perimeter.calc())

