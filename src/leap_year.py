def is_leap_year() -> bool:
    year1: int = int(input('Ingrese su año:'))
    if year1 % 4 == 0:
        if year1 % 400 == 0:
            print(f'El año {year1} es bisiesto')
            return True
        else:
            print(f'El año {year1} no es bisiesto')
            return False
    else:
        print(f'El año {year1} no es bisiesto')
        return False
