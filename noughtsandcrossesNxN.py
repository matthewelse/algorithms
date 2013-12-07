# Noughts and Crosses Game
size = 4

def print_grid(grid):
    for row in grid:
        output = ""
        for column in row:
            if column == 1:
                output += "O"
            elif column == 2:
                output += "X"
            else:
                output += "."
        print(output)

def winner(grid):
    winner = 0 
    diagonals = [[grid[i+j][i] for i in range(len(grid)) if i+j >= 0 and i+j < len(grid)] for j in range(3-len(grid), len(grid)-2)] + [[grid[i][len(grid)-1-(i+j)] for i in range(len(grid)) if len(grid)-1-(i+j) >= 0 and len(grid)-1-(i+j) < len(grid)] for j in range(3-len(grid), len(grid)-2)]
    
    # Check Rows...
    for y in range(0, len(grid)):
        count = 0
        player = 0
        
        for x in range(0, len(grid[0])):
            if grid[y][x] == player and player != 0:
                count += 1
            elif grid[y][x] != player and grid[y][x] != 0:
                player = grid[y][x]
                count = 1
            elif grid[y][x] == 0:
                count = 0
                player = 0
            
            if count == 3:
                winner |= player
                break
    
    # Check Columns...
    for x in range(0, len(grid)):
        count = 0
        player = 0
        
        for y in range(0, len(grid[0])):
            if grid[y][x] == player and player != 0:
                count += 1
            elif grid[y][x] != player and grid[y][x] != 0:
                player = grid[y][x]
                count = 1
            elif grid[y][x] == 0:
                count = 0
                player = 0
                
            if count == 3:
                winner |= player
                break
    
    # Check Diagonals
    for diagonal in diagonals:
        count = 0
        player = 0
        
        for cell in diagonal:
            if cell == player and player != 0:
                count += 1
            elif cell != player and cell != 0:
                player = cell
                count = 1
            
            if count == 3:
                winner |= player
                break 
    return winner

grid = [[0 for x in xrange(size)] for x in xrange(size)]
player = 1

while winner(grid) == 0:
    print_grid(grid)

    while True:
        try:
            print "Player %i's turn." % player
            position = raw_input()

            x = int(position[0])-1
            y = int(position[2])-1

            assert grid[y][x] == 0, "Invalid Move"
            grid[y][x] = player
            print grid
            break
        except (IndexError, ValueError, AssertionError):
            print("Invalid Move.")
    
    player = 1 if player == 2 else 2

print_grid(grid)
print "Player %i wins." % winner(grid)
