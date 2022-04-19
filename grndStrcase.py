def solver(n):
    combos = [0] * (n + 1)
    combos[0] = 1
    for i in range(1, n):
        for j in range(n, (i - 1), -1):
            combos[j] += combos[j - i]  
    return combos[n]

def grndStrcase(n):
    if n < 3:
        return 0
    return solver(n)
