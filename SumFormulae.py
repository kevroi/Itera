# Summing a constant n times
def consum(c, n):
    act = 0 # actual sum
    theo = 0 # theoretical sum
    for i in range(1, n+1):
        act += c
    theo = c * n
    print('Actual sum: ', act)
    print('Theoretical sum: ', theo)

# Summing first n natural numbers
def natsum(n):
    act = 0
    theo = 0
    for i in range(1, n+1):
        act += i
    theo = 1/2 * n * (n+1)
    print('Actual sum: ', act)
    print('Theoretical sum: ', theo)

# Summing first n squares
def squsum(n):
    act = 0
    theo = 0
    for i in range(1, n+1):
        act += i**2
    theo = 1/6 * n * (n+1) * (2*n+1)
    print('Actual sum: ', act)
    print('Theoretical sum: ', theo)

# Summing first n cubes
def cubsum(n):
    act = 0
    theo = 0
    for i in range(1, n+1):
        act += i**3
    theo = 1/4 * n**2 * (n+1)**2
    print('Actual sum: ', act)
    print('Theoretical sum: ', theo)