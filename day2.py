#advent of code day 2

# read in sub data
data_file = open('day2_submarine_data.txt')
depth_data = data_file.read().split()
data_file.close()

horiz_dist = 0
depth = 0
aim = 0

for i in range(0, len(depth_data), 2):
    if depth_data[i] == 'forward':
        horiz_dist += int(depth_data[i+1])
        depth += aim*int(depth_data[i+1])
    elif depth_data[i] == 'down':
        aim += int(depth_data[i+1])
    else: 
        aim -= int(depth_data[i+1])

print(horiz_dist)
print(depth)
print(horiz_dist*depth) #answer