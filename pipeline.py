import csv

def read_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    return rows