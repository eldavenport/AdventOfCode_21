# advent of code day 1
import numpy as np

# read in depth data
data_file = open('day1_depthdata.txt')
depth_data = data_file.read().split('\n')
data_file.close()

numerical_data = [eval(i) for i in depth_data]

numIncreases = 0
for item in range(len(numerical_data)):
    if numerical_data[item-1] < numerical_data[item]:
        numIncreases+= 1
    
print(numIncreases)

old_triplet = sum([numerical_data[0], numerical_data[1], numerical_data[2]])

num_triplet_increase = 0
for i in range(len(numerical_data)-2):
    new_triplet = sum([numerical_data[i], numerical_data[i+1], numerical_data[i+2]])
    if new_triplet > old_triplet:
        num_triplet_increase += 1
    old_triplet = new_triplet

print(num_triplet_increase)