rules = []
updates = []

with open("day5.txt") as file:
    finished = False
    while not finished:
        line = file.readline().removesuffix("\n")

        if line == "":
            finished = True
            break

        rules.append(line)

    updates = file.readlines()
    for u in range(len(updates)):
        updates[u] = updates[u].removesuffix("\n")

# process each update
sum_middle_page_number = 0
for update in updates:
    split = update.split(",")
    # first, check all the rules against it
    valid = True # True until proven False
    for rule in rules:
        r = rule.split("|")
        try:
            i1 = split.index(r[0])
            i2 = split.index(r[1])
            if not i1 < i2:
                valid = False
                break
        except ValueError:
            # ignore these errors; just means this rule doesn't apply to this update
            continue

    if not valid:
        continue

    # then, find the middle page number and add to sum
    sum_middle_page_number += int(split[(len(split) / 2).__floor__()])

print(f"Part 1: {sum_middle_page_number}")
