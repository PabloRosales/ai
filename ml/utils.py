import pathlib
from csv import reader

def load_csv(filename):
    filename = pathlib.Path(__file__).parent.parent / "data" / filename
    data = list()
    with open(filename, "r") as file:
        lines = reader(file)
        for row in lines:
            if not row:
                continue
            data.append(row)
    return data


def col2float(data, column):
    for row in data:
        row[column] = float(row[column].strip())


def col2int(data, column):
    classes = [row[column] for row in data]
    unique = set(classes)
    lookup = dict()

    for i, value in enumerate(unique):
        lookup[value] = i

    for row in data:
        row[column] = lookup[row[column]]

    return lookup


def minmax(data):
    mm = list()

    for i in range(len(data[0])):
        col_values = [row[i] for row in data]
        value_min = min(col_values)
        value_max = max(col_values)
        mm.append([value_min, value_max])

    return mm


def normalize(data, mm):
    for row in data:
        for i in range(len(row)):
            row[i] = (row[i] - mm[i][0]) / (mm[i][1] - mm[i][0])