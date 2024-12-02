# open the file
with open("day1.txt") as file:
    lines = file.readlines()

# read lines into left and right lists
left = []
right = []
for line in lines:
    s = line.removesuffix("\n").split(" ")
    left.append(int(s[0]))
    right.append(int(s[-1]))

# sort the location IDs
left.sort()
right.sort()

# find and summarise the distances
sum_distance = 0
for idx in range(left.__len__()):
    distance = abs(left[idx] - right[idx])
    sum_distance += distance

# Part 1
print(sum_distance)
