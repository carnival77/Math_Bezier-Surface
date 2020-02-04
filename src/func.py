import csv

def fileToMatrix(n, file):
    try:
        csvfile = open(file, newline='')
        spamreader = csv.reader(csvfile, delimiter=';')
    except Exception:
        return None

    matrix = []
    for _ in range(n):
        matrix.append([0.0] * n)
    empty = True
    try:
        for row in spamreader:
            empty = False
            matrix[int(row[1])][int(row[0])] = float(row[2])
    except Exception:
        return None
    if empty:
        return None
    return matrix

def solve(matrix, n, px, py):
    u = px / float(n - 1)
    v = py / float(n - 1)
    sol = 0
    for i in range(n):
        for j in range(n):
            bEqj = bEquation(n - 1, j, u) 
            bEqi = bEquation(n - 1, i, v) 
            point_ij = matrix[i][j]
            sol += bEqj * bEqi * point_ij

    return sol

def bEquation(n, i ,t):
    sol = binomial(n, i)
    sol *= t ** i
    sol *= (1 - t) ** (n - i)
    return sol

def binomial(n, i):
    if i <= 0:
        return 1
    sol = 1
    for x in range(n - i):
        sol *= x + i + 1
    sol /= fact(n - i)
    return sol

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n -1)