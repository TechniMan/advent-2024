reports = []

with open("day2.txt") as file:
    reports = file.readlines()

total_safe = 0
for report in reports:
    levels = list(map(int, report.removesuffix("\n").split(" ")))
    safe = False

    # all increasing
    previous = levels[0]
    for l in range(1, levels.__len__()):
        if levels[l] <= previous:
            safe = False
            break
        safe = True
        previous = levels[l]

    # OR all decreasing
    if safe == False:
        previous = levels[0]
        for l in range(1, levels.__len__()):
            if levels[l] >= previous:
                safe = False
                break
            safe = True
            previous = levels[l]

    # safe so far AND adjacent levels differ by at least one and at most three
    if safe == True:
        previous = levels[0]
        for l in range(1, levels.__len__()):
            diff = abs(levels[l] - previous)
            if diff < 1 or diff > 3:
                safe = False
                break
            safe = True
            previous = levels[l]

    if safe == True:
        total_safe += 1

print(total_safe)
