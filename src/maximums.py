def max_of_two(x: float, y: float) -> float:
    if x >= y:
        biggest: float = x
    else:
        biggest: float = y
    return biggest


def max_of_three(x: float, y: float, z: float) -> float:
    if x >= y and x >= z:
        biggest: float = x
    elif y >= z:
        biggest: float = y
    else:
        biggest: float = z
    return biggest
