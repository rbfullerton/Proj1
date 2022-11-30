import area
import perimeter

line = '---------------'


def selection():
    print(line + '\n SELECT SHAPE\n' + line)
    print('1 - Circle\n'
          '2 - Rectangle\n'
          '3 - Square\n'
          '4 - Triangle')


def main():
    selection()
    shape = input('Shape number:').strip()
    while shape not in ['1', '2', '3', '4']:
        shape = input('Shape number (1-4):').strip()

    comp = input('Computation (Area = 1 or Perimeter = 2):').strip()
    while comp not in ['1', '2']:
        comp = input('Enter 1 or 2:').strip()

    if shape == '1':
        if comp == '1':
            area.circle()
        elif comp == '2':
            perimeter.circle()
    elif shape == '2':
        if comp == '1':
            area.rectangle()
        elif comp == '2':
            perimeter.rectangle()
    elif shape == '3':
        if comp == '1':
            area.square()
        elif comp == '2':
            perimeter.square()
    elif shape == '4':
        if comp == '1':
            area.triangle()
        elif comp == '2':
            perimeter.triangle()
    pyexit()


def pyexit():
    exit_inp = input('Continue(y/n):').lower().strip()
    while exit_inp not in ['y', 'n']:
        exit_inp = input('Enter y or n:').lower().strip()
    if exit_inp == 'y':
        main()
    else:
        print('PROGRAM DONE')


if __name__ == '__main__':
    main()
