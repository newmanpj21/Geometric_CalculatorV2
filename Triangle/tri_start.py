from Triangle import area, perimeter

def operation():
    op = int(input('[1] Area\n'
                   '[2] Perimeter'))

    if op == 1:
        print(area.calc())
    elif op == 2:
        print(perimeter.calc())