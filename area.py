def circle():
    pi = 3.14
    radius = float(input('Circle radius:'))
    area = pi * (radius * radius)
    print('Circle Area = {:.2f}'.format(area))


def rectangle():
    length = float(input('Rectangle length:'))
    width = float(input('Rectangle width:'))
    area = length * width
    print('Rectangle Area = {:.2f}'.format(area))


def square():
    sides = float(input('Square side length:'))
    area = sides * sides
    print('Square Area = {:.2f}'.format(area))


def triangle():
    base = float(input('Triangle base:'))
    height = float(input('Triangle height:'))
    area = 0.5 * (base * height)
    print('Triangle Area = {:.2f}'.format(area))
