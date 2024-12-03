def is_report_safe(levels: list[int], tolerance: int = 1) -> bool:
    safe: bool = False

    # all increasing
    previous: int = levels[0]
    for l in range(1, levels.__len__()):
        if levels[l] <= previous:
            safe = False
            break
        safe = True
        previous = levels[l]

    # OR all decreasing; only check if above failed
    if not safe:
        previous = levels[0]
        for l in range(1, levels.__len__()):
            if levels[l] >= previous:
                safe = False
                break
            safe = True
            previous = levels[l]

    # either of above passed AND adjacent levels differ by at least one and at most three
    if safe:
        previous = levels[0]
        for l in range(1, levels.__len__()):
            diff = abs(levels[l] - previous)
            if diff < 1 or diff > 3:
                safe = False
                break
            safe = True
            previous = levels[l]

    return safe



reports = []

with open("day2.txt") as file:
    reports = file.readlines()

total_safe = 0
for report in reports:
    levels = list(map(int, report.removesuffix("\n").split(" ")))

    # check entire report is safe
    safe = is_report_safe(levels)

    # if unsafe, check iterations of the report to determine if it can be dampened
    if not safe:
        # unsafe until proven safe
        safe = False
        # retest, removing each level, to see if problem can be dampened
        # ign is level idx to ignore
        for ign in range(levels.__len__()):
            copy = levels.copy()
            copy.pop(ign)
            safe = is_report_safe(copy, 0)
            # if we had a completely safe run:
            if safe:
                break

    total_safe += safe
    if safe:
        #print("+ Safe: ", report.removesuffix("\n"))
        pass
    else:
        #print("- Unsafe: ", report.removesuffix("\n"))
        pass

print("Total: ", total_safe)
