import csv
import random

def generate_random_data(num_rows, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['OurESP1', 'OurESP2', 'OurESP3', 'x', 'y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for _ in range(num_rows):
            row = {
                'OurESP1': random.randint(1, 100),
                'OurESP2': random.randint(1, 100),
                'OurESP3': random.randint(1, 100),
                'x': random.uniform(0, 100),
                'y': random.uniform(0, 100)
            }
            writer.writerow(row)

num_rows = 10**5  # Change this to the desired number of rows
file_name = 'random_data.csv'

generate_random_data(num_rows, file_name)
