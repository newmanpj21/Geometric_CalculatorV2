from Circle import circ_start
from Rectangle import rec_start
from Rhombus import rhom_start
from Trapezoid import trap_start
from Triangle import tri_start

print('\n'
      'Welcome to the Geometric Calculator'
      '\n'
      )

shape = int(input('[1] Circle\n'
                  '[2] Rectangle\n'
                  '[3] Rhombus\n'
                  '[4] Trapezoid\n'
                  '[5] Triangle\n'))

if shape == 1:
    print(circ_start.operation())

elif shape == 2:
    print(rec_start.operation())

elif shape == 3:
    print(rhom_start.operation())

elif shape == 4:
    print(trap_start.operation())

elif shape == 5:
    print(tri_start.operation())