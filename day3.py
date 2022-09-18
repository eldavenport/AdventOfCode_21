# advent of code day 3

from math import gamma
import numpy as np


data_file = open('day3_input.txt')
binary_data = data_file.read().split()
data_file.close()
numBits = 12

gamma_rate = np.zeros(12)
epsilon_rate = np.zeros((12))

organized_data = np.zeros((len(binary_data),12))

for i in range(len(binary_data)):
    organized_data[i,:] = [int(i) for i in str(binary_data[i])]

numRows = np.shape(organized_data)[0]


for i in range(numBits):
    for j in range(numRows):
        gamma_rate[i] += organized_data[j,i]

for bit in range(12):
    if gamma_rate[bit] > numRows/2:
        gamma_rate[bit] = 1
        epsilon_rate[bit] = 0
    else:
        gamma_rate[bit] = 0
        epsilon_rate[bit] = 1


gamma_rate = int('101110100101', 2)
epsilon_rate = int('010001011010', 2)

print(gamma_rate)
print(epsilon_rate)
print(gamma_rate*epsilon_rate)
