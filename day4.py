width = 140

# read into grid
grid: list[list[str]] = []
with open("day4.txt") as file:
    for line in file.readlines():
        l: list[str] = []
        for c in line:
            l.append(c)
        if l.__len__() == 141:
            l.remove('\n')
        grid.append(l)

# conduct word search for 'XMAS'
sum = 0
sum_p2 = 0
for y in range(width):
    for x in range(width):
        # is this the start of an 'XMAS'?
        if grid[y][x] == 'X':

            ## HORIZONTAL
            if x >= 3:
                # can search left
                if grid[y][x - 1] == 'M' and grid[y][x - 2] == 'A' and grid[y][x - 3] == 'S':
                    sum += 1
            if x <= width - 4:
                # can search right
                if grid[y][x + 1] == 'M' and grid[y][x + 2] == 'A' and grid[y][x + 3] == 'S':
                    sum += 1

            ## VERTICAL
            if y >= 3:
                # can search up
                if grid[y - 1][x] == 'M' and grid[y - 2][x] == 'A' and grid[y - 3][x] == 'S':
                    sum += 1
            if y <= width - 4:
                # can search down
                if grid[y + 1][x] == 'M' and grid[y + 2][x] == 'A' and grid[y + 3][x] == 'S':
                    sum += 1

            ## DIAGONAL
            if x >= 3 and y >= 3:
                # can search up-left
                if grid[y - 1][x - 1] == 'M' and grid[y - 2][x - 2] == 'A' and grid[y - 3][x - 3] == 'S':
                    sum += 1
            if x <= width - 4 and y <= width - 4:
                # can search down-right
                if grid[y + 1][x + 1] == 'M' and grid[y + 2][x + 2] == 'A' and grid[y + 3][x + 3] == 'S':
                    sum += 1
            if x >= 3 and y <= width - 4:
                # can search down-left
                if grid[y + 1][x - 1] == 'M' and grid[y + 2][x - 2] == 'A' and grid[y + 3][x - 3] == 'S':
                    sum += 1
            if x <= width - 4 and y >= 3:
                # can search up-right
                if grid[y - 1][x + 1] == 'M' and grid[y - 2][x + 2] == 'A' and grid[y - 3][x + 3] == 'S':
                    sum += 1

        # is this the start of an 'X-MAS'?
        if grid[y][x] == 'M':
            # * M
            #  A 
            # S S
            if y <= width - 3 and x <= width - 3:
                if grid[y][x + 2] == 'M':
                    if grid[y + 1][x + 1] == 'A':
                        if grid[y + 2][x] == 'S' and grid[y + 2][x + 2] == 'S':
                            sum_p2 += 1

            # S *
            #  A 
            # S M
            if y <= width - 3 and x >= 2:
                if grid[y + 2][x] == 'M':
                    if grid[y + 1][x - 1] == 'A':
                        if grid[y + 2][x - 2] == 'S' and grid[y][x - 2] == 'S':
                            sum_p2 += 1

            # S S
            #  A 
            # M *
            if y >= 2 and x >= 2:
                if grid[y][x - 2] == 'M':
                    if grid[y - 1][x - 1] == 'A':
                        if grid[y - 2][x - 2] == 'S' and grid[y - 2][x] == 'S':
                            sum_p2 += 1

            # M S
            #  A 
            # * S
            if y >= 2 and x <= width - 3:
                if grid[y - 2][x] == 'M':
                    if grid[y - 1][x + 1] == 'A':
                        if grid[y - 2][x + 2] == 'S' and grid[y][x + 2] == 'S':
                            sum_p2 += 1

print(f"Part 1: {sum}")
print(f"Part 2: {sum_p2}")
