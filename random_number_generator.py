import csv
import random

random_numbers = [random.randint(0, 9999) for _ in range(1000)]

with open('random_numbers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for num in random_numbers:
        writer.writerow([str(num)])
