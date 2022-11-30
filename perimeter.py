def circle():
    pi = 3.14
    radius = float(input('Circle radius:'))
    per = 2 * (pi * radius)
    print('Circle Perimeter = {:.2f}'.format(per))


def rectangle():
    length = float(input('Rectangle length:'))
    width = float(input('Rectangle width:'))
    per = 2 * (length * width)
    print('Rectangle Perimeter = {:.2f}'.format(per))


def square():
    sides = float(input('Square side length:'))
    per = 4 * sides
    print('Square Perimeter = {:.2f}'.format(per))


def triangle():
    side1 = float(input('Triangle side 1:'))
    side2 = float(input('Triangle side 2:'))
    side3 = float(input('Triangle side 3:'))
    per = (side1 + side2 + side3)
    print('Triangle Perimeter = {:.2f}'.format(per))
