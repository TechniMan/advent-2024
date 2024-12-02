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

sum_distance = 0
similarity_score = 0
for idx in range(left.__len__()):
    # find and summarise the distances
    distance = abs(left[idx] - right[idx])
    sum_distance += distance

    # determine similarity score
    similarity_score += left[idx] * right.count(left[idx])

# Part 1
print(sum_distance)
# Part 2
print(similarity_score)
