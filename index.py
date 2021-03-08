import math
import csv

with open('data.csv') as d:
    reader = csv.reader(d)
    file_data = list(reader)

data = file_data[0]
population_size = len(data)
SQUARED_LIST = []


def mean():
    tot = 0
    for i in data:
        tot += int(i)
    return tot / population_size


MEAN = mean()

for i in data:
    x = float(i) - MEAN
    SQUARED_LIST.append(x**2)

STANDARD_DERIVATION = math.sqrt(sum(SQUARED_LIST) / population_size)
print(STANDARD_DERIVATION)
