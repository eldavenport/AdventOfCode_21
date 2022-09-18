# day 3 part 2# advent of code day 3

from math import gamma
from tkinter.tix import COLUMN
import numpy as np


data_file = open('day3_input.txt')
binary_data = data_file.read().split()
data_file.close()
numBits = 12

oxygen = np.zeros(12)
co2 = np.zeros((12))

organized_data = np.zeros((len(binary_data),12))

for i in range(len(binary_data)):
    organized_data[i,:] = [int(i) for i in str(binary_data[i])]

numRows = np.shape(organized_data)[0]

oxygen_indices = []
oxygen_data = organized_data
co2_data = organized_data
co2_indices = []

for bit in range(numBits):
    column_total = 0
    column_total_co2 = 0
    co2_indices = []
    oxygen_indices = []

    if np.shape(oxygen_data)[0] != 1:
        # print(np.shape(oxygen_data)[0])
        for j in range(np.shape(oxygen_data)[0]):
            column_total += oxygen_data[j][bit]
        pass

        if column_total > (np.shape(oxygen_data)[0])/2:
            oxygen_flag = 1
        elif column_total == (np.shape(oxygen_data)[0])/2:
            oxygen_flag = 1
        else:
            oxygen_flag = 0

        for j in range(np.shape(oxygen_data)[0]):
            if oxygen_data[j][bit] == oxygen_flag:
                oxygen_indices.append(j)
        pass
        oxygen_data = [oxygen_data[index] for index in oxygen_indices]

    if np.shape(co2_data)[0] != 1:
        # print(np.shape(co2_data)[0])
        for j in range(np.shape(co2_data)[0]):
            column_total_co2 += co2_data[j][bit]
        pass
    
        if column_total_co2 > (np.shape(co2_data)[0])/2:
            co2_flag = 0
        elif column_total_co2 == (np.shape(co2_data)[0])/2:
            co2_flag = 0
        else:
            co2_flag = 1

        for j in range(np.shape(co2_data)[0]):
            if co2_data[j][bit] == co2_flag:
                co2_indices.append(j)
        pass
        co2_data = [co2_data[index] for index in co2_indices]
pass

# print("co2 = ",co2_data)
# print("oxygen = ",oxygen_data)

oxygen_rate = int('101011101111', 2)
co2_rate = int('011001000001', 2)

print(oxygen_rate)
print(co2_rate)
print(oxygen_rate*co2_rate)
