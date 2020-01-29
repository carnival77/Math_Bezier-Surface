import csv
def fileToMatrix(n, file):
    try:
        csvfile = open(file, newline='')
        spamreader = csv.reader(csvfile, delimiter=';')
    except Exception:
        return None

    matrix = []
    for i in range(n):
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