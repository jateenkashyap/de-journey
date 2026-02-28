import csv

def read_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    return rows

def count_rows(rows):
    return len(rows)

def main():
    filename = "data.csv"
    rows = read_data(filename)
    print(f"Total rows processed: {count_rows(rows)}")

main()