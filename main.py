from Figures import *

Figures = Figures('Figures')
Coan = Coan('coan', 32)
parallelepiped = parallelepiped('parallelepiped', 21)
cube = cube('cube', 32)
sphere = sphere('sphere', 4)
elipse = elipse('elipse', 22)
culindr = culindr('culindr', 23)


def print_Figures():
    print(Figures.name)
    print(Coan.get_info())
    print(parallelepiped.get_info())
    print(cube.get_info())
    print(sphere.get_info())
    print(elipse.get_info())
    print(culindr.get_info())


print_Figures()