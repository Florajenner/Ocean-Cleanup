# Ocean Cleanup Game

## Overview
The Ocean Cleanup Game is an interactive, console-based game that aims to educate and engage players in an environment-friendly activity - cleaning up the ocean. Players are challenged to locate and clean up rubbish in a virtual ocean grid within a limited number of guesses. This game is a fun way to raise awareness about the global issue of ocean pollution.

## Getting Started

### Installation
- Clone the repository to your local machine and navigate to the project directory in the terminal. You can then run the game by executing the command `python game.py`.

## How to Play
Upon starting the game, players are greeted with a narrative that sets the context for the gameplay. Players then enter their name and are presented with a 10x10 grid representing the ocean, where some cells contain plastic rubbish denoted by 'P'.

Players are given 10 attempts to guess the location of the rubbish on the grid. For each guess, players enter a coordinate (e.g., C4), aiming to locate a piece of rubbish. When a player successfully locates rubbish, it is marked with an 'X' on the grid.

The game continues until all guesses are used up, after which the game reveals the remaining rubbish on the grid and provides a score based on the number of pieces of rubbish the player was able to clean up.

## Deploying on Heroku

### Steps to Deploy:
1. Navigate to the Heroku website and sign up for an account.
2. Once logged in, click on the "New" button to create a new app.
3. Enter a unique name for your app in the "App name" field.
4. Select your geographical region from the "Choose region" dropdown menu.
5. Click on the "Create App" button to proceed.
6. After being redirected, navigate to the "Settings" tab.
7. Under the settings, find and click on the "Config Vars" section.
8. Add a new configuration variable with a key of PORT and a value of 8000, then click the "Add" button.
9. Now, it's time to add Buildpacks. Click on the "Add Buildpack" button.
10. Add the Python buildpack first, followed by the Node.js buildpack.
11. Once the buildpacks are added, head over to the "Deploy" tab.
12. In the deploy screen, choose GitHub as the deployment method and link your GitHub profile.
13. Search for and select the repository you wish to deploy to Heroku, then click "Connect".
14. After connecting the repository, you can opt for either manual or automatic deployment.
15. By opting for automatic deploys, Heroku will create a new build of the app whenever changes are pushed to the repository.
16. Upon a successful build, a link to the live site will be provided by Heroku. Click on the link to visit the deployed site.

## Code Structure
The code is structured into several functions, each encapsulating a specific part of the game logic or user interaction:

- `create_ocean()`: Creates the initial ocean grid.
- `print_game_board(grid)`: Prints the current state of the ocean grid.
- `get_user_guess()`: Prompts the player for a coordinate guess and validates the input.
- `get_player_name()`: Gets and validates the player's name.
- `intro_game()`: Provides the game introduction and starts the game loop.
- `game_loop(player_name)`: Contains the main game loop, handling player guesses and tracking the game state.

## Customization
Players can customize the game by modifying the `ROWS`, `COLS`, and `AMOUNT_OF_RUBBISH` variables at the beginning of the code to change the grid dimensions and the amount of rubbish in the ocean.

## Testing
The testing phase is crucial to ensure that each function within the application behaves as expected. Below is a table that outlines the various tests carried out, the actions performed, the expected outcomes, and the results of each test.

| TEST             | ACTION                                                  | EXPECTATION                                                        | RESULT  |
|------------------|---------------------------------------------------------|-------------------------------------------------------------------|---------|
| create_ocean()   | Call function                                           | Returns a 2D grid with specified dimensions and rubbish count     | Pass|
| print_game_board() | Call function with a grid argument                   | Prints the grid to console in a readable format                    | Pass|
| get_user_guess() | Call function                                           | Returns a validated coordinate or prompts user again for input     | Pass|
| game_loop()      | Call function with a player name argument              | Handles player guesses, updates grid, and tracks game state       | Pass|
| get_player_name()| Call function                                           | Returns a validated player name or prompts user again for input    | Pass|
| intro_game()     | Call function                                           | Provides game introduction and starts the game loop               | Pass|

### Pep8 Testing
All clear, no errors found.
![Pep8](/images/pep8.png)


## Credits

### Working with Characters and Unicode code points:
Conversion between characters and their Unicode code points using the `ord` function is observed in the `game_loop` function.

Reference: [Python ord() function](https://stackoverflow.com/questions/67697669/alphabetical-grid-using-python3).

### Working with Sets:
The `previous_guesses` set is utilized to record the user's past guesses. Sets store unique elements and checking for existence in a set is faster than in a list.

Reference: [Python Sets](https://www.w3schools.com/python/python_sets.asp).

### Books
Python For GCSE Computer Science Programming Guide by CGP, Python Crash Course (2nd Edition) by Eric Matthes

## Next Stages
In the future improvements could be made by giving players the option to select easy, medium or hard at the start of the game.

## Contributing
Feel free to fork the project and submit pull requests for any bug fixes or feature enhancements. All contributions are welcome!

## Acknowledgements
My Mentor, Spencer Barriball, for his thoughtful and helpful feedback.
Tutor support at Code Institute for their support and assistance.
