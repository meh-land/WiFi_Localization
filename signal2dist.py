import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        for row in csvreader:
            data.append(row)
    return data

# Example usage:
filename = 'signals.temp'  # Replace 'your_csv_file.csv' with the actual filename
csv_data = read_csv_file(filename)
print(csv_data)
