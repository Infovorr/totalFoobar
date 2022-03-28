def fuelIP(n):
    number = int(n)
    total = 0
    while number > 1:
        if (number == 3) or (number % 4 == 1):
            number -= 1
            number //= 2
            total += 2
        elif (number % 2 == 0):
            number //= 2
            total += 1
        else:
            number += 1
            total += 1
    return total
