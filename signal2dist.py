import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            for i in range(len(row)):
                row[i] = row[i].strip()
            data.append(row)
    return data

# Example usage:
filename = 'signals.temp'
csv_data = read_csv_file(filename)
# sig_str is strength in dbm, sig_lev is the level of the signal (1< siglev < 100)
sig_str = []
for j in range(len(csv_data)):
    sig_lev = float(csv_data[j][1])
    curr_sig_str = (sig_lev / 2) - 100
    sig_str.append(curr_sig_str)
print(sig_str)
