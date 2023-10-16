import random
import re

# Define grid dimensions
ROWS, COLS = 10, 10
AMOUNT_OF_RUBBISH = 0.4
grid = []


def create_ocean():
    """
    This function creates the 2D game board
    """
    # Number of 'P' cells board will have plastic rubbish in
    num_plastic = int(AMOUNT_OF_RUBBISH * ROWS * COLS)

    # Create a 1D list with 'P' and empty spaces
    grid_list = ['P'] * num_plastic + ['-'] * (ROWS*COLS - num_plastic)

    # Shuffle the list
    random.shuffle(grid_list)

    # Convert the shuffled list to 2D grid
    return [grid_list[i:i+COLS] for i in range(0, len(grid_list), COLS)]


def print_game_board(game_board):
    """
    This function prints the game grid
    """
    print('======= OCEAN =========')
    for row in game_board:
        print(' '.join(row))
    print('=======================')


def get_user_guess():
    """
    This function gets the user's guess and validates it.
    """
    while True:
        guess = input("Enter your guess (A-J, 1-10):\n").strip().upper()
        if not re.match(r'^[A-J](10|[1-9])$', guess):
            print(
                """
                Invalid input. Please enter a letter between A and J and a
                number between 1 and 10.
                """
                )
            print(
                """
                Hint: The letter should be between A and J, and the number
                should be between 1 and 10.
                """
                )
        else:
            return guess[0], int(guess[1:])


def get_player_name():
    """
    This function gets the players name and validates that it isn't empty.
    """
    player_name = input('Please can I have your name?\n').strip().lower()
    while player_name == '':
        player_name = input('''
                            Hey you cannot enter nothing,
                            This really does prove my point that humans are
                            stupid - try again, your name?''').strip().lower()
    return player_name


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
    player_name = get_player_name()
    global grid
    grid = create_ocean()
    game_loop(player_name)


def game_loop(player_name):
    """
    This function contains the main game loop
    """
    previous_guesses = set()
    num_guesses = 0
    num_rubbish = 0

    while num_guesses < 10:
        guess_row, guess_col = get_user_guess()
        guess = (guess_row, guess_col)

        if guess in previous_guesses:
            print(f"Sorry {player_name}, you've already guessed that spot.")
            continue

        previous_guesses.add(guess)
        num_guesses += 1

        if grid[ord(guess_row) - ord('A')][guess_col - 1] == 'P':
            print(f'Well done {player_name}, you found some rubbish!')
            num_rubbish += 1
            # Replace the 'P' with 'X' to show that the rubbish has been found
            grid[ord(guess_row) - ord('A')][guess_col - 1] = 'X'
        else:
            print(f'Sorry {player_name}, there is no rubbish there.')

    print(
        f'Game over, {player_name}! You found {num_rubbish} bits of rubbish.'
        )

    # Display the game board with the plastic that the player has managed to
    # find marked with an 'X', and the plastic they did not find marked with
    # a 'P'
    print('======= OCEAN =========')
    for row in grid:
        row_str = ''
        for cell in row:
            if cell == 'X':
                row_str += cell + ' '
            else:
                row_str += cell + ' '
        print(row_str.strip())
    print('=======================')


if __name__ == '__main__':
    intro_game()