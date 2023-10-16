import random
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
​
​
def print_game_board(grid):
    """
    This function prints the game grid
    """
    print('======= OCEAN =========')
    for row in grid:
        print(' '.join(row))
    print('=======================')
​
​
def intro_game():
    """
    This explains teh concept of the game and starts it
    """
    print('''
          Welcome traveller, the Earth need your help.
          The stupid humans have left their plastics in the ocean...
          You need to prove humans aren't all bad and we are going to have a
          contest between you and I as to who is going to pick up most the
          litter.
          First of all I need to get something from you.''')
    get_player_name()
​
​
def get_player_name():
    """
    This function gets the players name and validates that it isn't empty.
    """
    player_name = input('Please can I have your name?').strip().lower()
    while player_name == '':
        player_name = input('''
                            Hey you cannot enter nothing,
                            This really does prove my point that humans are
                            stupid - try again, your name?''').strip().lower()
    grid = create_ocean()
    print_game_board(grid)
​
    game_loop(player_name)

def get_user_guess():
    """
    This function gets the user's guess and validates it.
    """
    while True:
        guess = input("Enter your guess (A-J, 1-10): ").strip().upper()
        if len(guess) != 2 or not ('A' <= guess[0] <= 'J') or not (1 <= int(guess[1:]) <= 10):
            print("Invalid input. Please enter a letter between A and J and a number between 1 and 10.")
            print("Hint: The letter should be between A and J, and the number should be between 1 and 10.")
        else:
            return guess[0], int(guess[1:])    
​
​
def game_loop(player_name):

    # Create a set to track previous guesses and avoid duplicate guesses.
    previous_guesses = set()
    num_guesses = 0
    num_rubbish = 0

     while num_guesses < 5:
    guess_row, guess_col = get_user_guess()
    guess = (guess_row, guess_col)

    print(f'Well hello {player_name}, let us see what you have got') 
                        