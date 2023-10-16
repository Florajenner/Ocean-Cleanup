​
# Define grid dimensions
ROWS, COLS = 10, 10
AMOUNT_OF_RUBBISH = 0.4
grid = []

​
​
def create_ocean():
    """
    This function creates the 2D game board
    """
    # Number of 'P' cells board will have plastic rubbish in
    num_P = int(AMOUNT_OF_RUBBISH * ROWS * COLS)
​
    # Create a 1D list with 'P' and empty spaces
    grid_list = ['P'] * num_P + ['-'] * (ROWS*COLS - num_P)
​
    # Shuffle the list
    random.shuffle(grid_list)
​
    # Convert the shuffled list to 2D grid
    grid = [grid_list[i:i+COLS] for i in range(0, len(grid_list), COLS)]
    return grid