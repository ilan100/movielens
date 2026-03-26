import os
import areas
import platform
import getpass
import sys

k = 100

def check_global_names(name: str) -> bool:
    return name in globals()

def print_args() -> None:
    for arg in sys.argv[:0:-1]:
        print(arg)

#----------------------------------------------------------------------------------------
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(globals())

# EX1
    print('\nEX1\nk in globals: ', check_global_names('k'))
    print('j in globals: ', check_global_names('j'))

# EX2
    width = 10
    height = 12
    radius = 8
    print('\nEX2\ncircle area with raduis:', radius, 'is:',
          areas.circle_area(radius))
    print('triangle area with width:', width, 'and height:', height, 'is:',
          areas.triangle_area(width, height))
    print('rectangle area with width:', width, 'and height:', height, 'is:',
          areas.circle_area(radius))

# EX3
    print('\nEX3')
    print(platform.system())
    print(platform.platform())
    print(getpass.getuser())
    print(os.getcwd())

# EX4
    print('\nEX4')
    print_args()

# EX5
# this is implemented in exec_permit.py as an independent script