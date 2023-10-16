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

def print_game_board(grid):
    """
    This function prints the game grid
    """
    print('======= OCEAN =========')
    for row in grid:
        print(' '.join(row))
    print('=======================')

def intro_game():
    """
    This explains the concept of the game and starts it
    """
    print('''
          Welcome traveller, the Earth need your help.
          The stupid humans have left their plastics in the ocean...
          You need to prove humans aren't all bad and we are going to have a
          contest between you and I as to who is going to pick up most the
          litter.
          First of all I need to get something from you.''')    

def get_player_name():
    """
    This function gets the players name and validates that it isn't empty.
    """
    player_name = input('Please can I have your name?').strip().lower()          