# -*- coding: utf-8 -*-
"""Random_number_generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13XIEDXz0qQ3DXyWLSgO5Afgi4O9oOfGV
"""

import csv
import random

random_numbers = [random.randint(0, 9999) for _ in range(1000)]

with open('random_numbers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for num in random_numbers:
        writer.writerow([str(num)])