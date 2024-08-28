def is_leap_year() -> bool:
    year: int = int(input("Ingrese un año: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        bisiesto_message: str = "es bisiesto"
        result: bool = True
    else:
        bisiesto_message: str = "no es bisiesto"
        result: bool = False

    print(f"El año {year} {bisiesto_message}")
    return result
