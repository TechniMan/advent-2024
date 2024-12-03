from itertools import pairwise


def is_report_safe(levels: list[int]) -> bool:
    # all increasing OR decreasing
    safe = sorted(levels) == levels or sorted(levels, reverse=True) == levels

    # AND adjacent levels differ by at least one and at most three
    return safe and all(1 <= abs(b - a) <= 3 for a, b in pairwise(levels))


reports: list[str]
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
            safe = is_report_safe(copy)
            # if we had a completely safe run:
            if safe:
                break

    total_safe += safe
    if safe:
        #print(f"+ Safe: {report.removesuffix("\n")}")
        pass
    else:
        #print(f"- Unsafe: {report.removesuffix("\n")}")
        pass

print("Total: ", total_safe)
