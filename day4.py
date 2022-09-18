from math import gamma
from tkinter import N
from tkinter.tix import COLUMN
from turtle import pu
import numpy as np

numbers_file = open('day4_input_numbers.txt')
number_data = numbers_file.read().split(',')
numbers_file.close()

boards_file = open('day4_input_boards.txt')
boards_data = boards_file.read().split()
boards_file.close()

num_boards = int(len(boards_data)/25)
boards = np.zeros((num_boards, 5, 5))

dataIndex = 0
for i in range(num_boards):
    boards[i][0] = boards_data[dataIndex:dataIndex+5]
    boards[i][1] = boards_data[dataIndex+5:dataIndex+10]
    boards[i][2] = boards_data[dataIndex+10:dataIndex+15]
    boards[i][3] = boards_data[dataIndex+15:dataIndex+20]
    boards[i][4] = boards_data[dataIndex+20:dataIndex+25]
    dataIndex = dataIndex + 25

bingo = -1
winning_num = 0
for number in number_data:
    indices = np.where(boards == int(number))
    for a in range(np.shape(indices)[1]):
        index1 = indices[0][a]
        index2 = indices[1][a]
        index3 = indices[2][a]
        boards[index1][index2][index3] = -1
    for n in range(num_boards):
        for row in range(5):
            print(np.shape(np.where(boards[n][row][:] == -1))[1])
            if (np.shape(np.where(boards[n][row][:] == -1))[1]) == 5:
                bingo = n
                winning_num = number
                break
            elif (np.shape(np.where(boards[n][:][row] == -1))[1]) == 5:
                bingo = n
                winning_num = number
                break
        if bingo != -1:
            break
    if bingo != -1:
        break

puzzle_sum = 0
for row in range(5):
    for col in range(5):
        if boards[bingo][row][col] != -1:
            puzzle_sum += boards[bingo][row][col]

print(int(puzzle_sum)*int(winning_num))
