#circle
from Circle import circ, area


def operation():
    op = int(input('[1] Area\n'
                   '[2] Perimeter\n'))
    if op == 1:
        print('The area is: ', area.area())
    elif op == 2:
        print('The circumference is: ', circ.circ())

