# suduko solving abcktracking algorithm

# 1 - print the board
# 9x9 board
# store each row of the board in an array
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7] 
]
# 2 - print the board in grid format
def print_board(bo):
    #printing horizontal markings
    for i in range(len(bo)):
        # if i modulus 3 is equal -> 0 & i is not = 0 then print out the grid markings
        # this will print out the grid markings every 3 rows
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
    #printing vertical markings
    # loop through elements when j is in range of board pos[0]
        for j in range(len(bo[0])):
            # if j modulus 3 is = 0 || j not = 0 then print a vertical line
            # this will print out a vertical line every 3 elemets to give an illusion of 3 vertical lines across the board
            if j % 3 == 0 and j != 0:
                print(' | ', end ="")

            if j == 8:
                print(bo[i][j])
            else: 
                print(str(bo[i][j]) + " ", end ="")

#3 - find an empty box in the grid 
def find_empty(bo):    
    #find an empty box in the row 
    for i in range(len(bo)):
        # find the empty box in the col
        for j in range(len(bo[0])):
            # if the number in pos[i][j] = 0 return the pos
            # i = row 
            # j = col
            if bo[i][j] == 0:
                return (i,j)
    return None   


# 4  - solve function 
def solve(bo):
    #finds the first empty box in row
    find = find_empty(bo)
    # if not 0 then return true to mark the pos as filled
    if not find:
        return True
    #else find the row / col pos    
    else: 
        row, col = find

    # finding a possible solution from the num 1-9
    #recursive function which calls its self from within its own function
    # recursivly call solve until board is solved
    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i  
            if solve(bo):
                return True
            bo[row][col] = 0 
    return False        

# 5 - is input valid
def valid(bo,num,pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i]== num and pos[1] != i:
            return False
    #Check  col 
    for i in range(len(bo)):
        if bo[i][pos[1]]== num and pos[0] != i:    
            return False
    #check 3x3 grid
    #int division to find the 3x3 area to check
    box_x = pos[1] // 3
    box_y = pos[0] // 3  

    for i in range(box_y * 3 , box_y * 3 + 3):
        for j in range(box_x *3 , box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True            


# 6 - applying algorithm to board 
print('')
print("starting board")
print_board(board)
solve(board)
print('')
print('////////////////////////')
print('')
print("solved board")
print('')
print_board(board)