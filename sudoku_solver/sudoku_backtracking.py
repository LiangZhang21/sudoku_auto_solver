
# Search the matrix location of the empty spot
def check_empty_spot(arr, empty_location):
    for i in range(9):
        for j in range(9):
            if (arr[i][j] == 0):
                empty_location[0] = i
                empty_location[1] = j
                return True
    return False

# check row is safe
def check_row(arr, row, num):
    for i in range(9):
        if (arr[row][i] == num):
            return False
    return True

# check col is safe
def check_col(arr, col, num):
    for i in range(9):
        if (arr[i][col] == num):
            return False
    return True

# check box is safe
def check_box(arr, row, col, num):
    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if (arr[box_row + i][box_col + j] == num):
                return False
    return True

def is_safe(arr, row, col, num):
    return check_row(arr, row, num) and check_col(arr, col, num) and check_box(arr, row, col, num)

def solve_sudoku(arr):
    #use 2-D matrix the identify the location of the empty spot 
    empty_location = [0, 0]

    if (not check_empty_spot(arr, empty_location)):
        return True
    
    row = empty_location[0]
    col = empty_location[1]

    for num_to_fill in range(1, 10):
        if (is_safe(arr, row, col, num_to_fill)):
            arr[row][col] = num_to_fill
            if (solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False

def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end = " ")
        print("")

# Driver main function to test above functions
if __name__ == "__main__":
	
	# assigning values to the grid
    # "0" represents the empty spots 
	grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]
	
	# if success print the grid
	if(solve_sudoku(grid)):
		print_grid(grid)
	else:
		print("No solution exists")

# The above code is referenced from Harshit Sidhwa.
