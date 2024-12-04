import re


input: str
with open("day3.txt") as file:
    input = file.read()

muls = re.findall("mul\((\d{1,3}),(\d{1,3})\)", input)

sum_p1 = 0
for mul in muls:
    sum_p1 += (int(mul[0]) * int(mul[1]))

print(f"Part 1: {sum_p1}")

matches = re.findall("(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", input)
sum_p2 = 0
mul_enabled = True
for match in matches:
    if match[0] == "do()":
        mul_enabled = True
    elif match[0] == "don't()":
        mul_enabled = False
    elif mul_enabled:
        sum_p2 += (int(match[1]) * int(match[2]))

print(f"Part 2: {sum_p2}")
