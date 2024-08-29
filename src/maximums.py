def max_of_two(x: int, y: int) -> int:
    biggest: int = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest

# Replace the "ANSWER HERE" for your answer
def max_of_three(x: int, y: int, z: int) -> int:
    if y < x > z:
        return x
    elif x < y > z:
        return y
    else:
        return z