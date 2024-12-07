grid_width = 130

with open("day6.txt") as file:
    lines = file.readlines()
    grid = list(map(lambda line: list(line.removesuffix("\n")), lines))

# find starting pos
start_pos = []
for y in range(grid_width):
    for x in range(grid_width):
        if grid[y][x] == "^":
            start_pos = [x, y]
            break
    if start_pos:
        break

# move guard around the grid
should_continue = True
facing = [0, -1] # [x, y]
pos = start_pos
while should_continue:
    # are we going out of bounds?
    if pos[0] + facing[0] < 0 or pos[0] + facing[0] >= grid_width or pos[1] + facing[1] < 0 or pos[1] + facing[1] >= grid_width:
        # move forward, out of the grid
        grid[pos[1]][pos[0]] = "X"
        should_continue = False
        break
    new_location = grid[pos[1] + facing[1]][pos[0] + facing[0]]
    if new_location == "#":
        if facing[0] == 0:
            # turn around - vertical
            if facing[1] == 1:
                # down
                facing = [-1, 0]
            else:
                # up
                facing = [1, 0]
        else:
            # - horizontal
            if facing[0] == 1:
                # right
                facing = [0, 1]
            else:
                # left
                facing = [0, -1]
    else:
        # move forward
        grid[pos[1]][pos[0]] = "X"
        pos = [pos[0] + facing[0], pos[1] + facing[1]]

# tally up total X spaces
total_x = 0
for y in range(grid_width):
    for x in range(grid_width):
        if grid[y][x] == "X":
            total_x += 1

print(f"Part 1: {total_x}")
