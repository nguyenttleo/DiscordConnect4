# DiscordConnect4

Welcome to DiscordConnect4! This project allows users to play the classic game of Connect 4 with each other on Discord. The game logic is implemented in `game.py`, while the Discord bot automation is handled in `main.py`.

## Project Overview

DiscordConnect4 enables users to engage in a competitive game of Connect 4 on Discord. Connect 4 is a two-player game where the objective is to be the first to connect four of your colored discs in a row, either horizontally, vertically, or diagonally on the game board.

The project consists of the following files:

- `main.py`: This file automates the Discord bot to facilitate the game interactions and commands.
- `game.py`: This file contains the game logic and functions for Connect 4.
- `gameboard.txt`: This file represents the current state of the game board.
- `gamenumber.txt`: This file keeps track of the number of games played.
- `welcome.txt`: This file contains a welcome message for new players.
- `endgame.txt`: This file contains a message for the end of the game.
- `newboard.txt`: This file contains an empty Connect 4 board.

## How to Play

Connect 4 is played on a vertical grid of 6 rows and 7 columns. The game board is represented using emojis:

```
🔴⚪⚪⚪⚪⚪⚪
🔴⚪⚪⚪⚪⚪⚪
🔴⚪⚪⚪⚪⚪⚪
🔴⚪⚪⚪⚪⚪⚪
🔴⚪⚪⚪⚪⚪⚪
🔴⚪⚪⚪⚪⚪⚪
```

- Player 1 is represented by the red emoji (🔴), and Player 2 is represented by the white emoji (⚪).
- Players take turns dropping their colored discs into one of the seven columns.
- The disc will fall to the lowest available space in the selected column.
- The first player to connect four of their discs in a row (horizontally, vertically, or diagonally) wins the game.
- If all columns are filled and no player has won, the game ends in a draw.

## Setup and Usage

To set up and use the DiscordConnect4 project, follow these steps:

1. Clone the project repository:

   ```bash
   git clone https://github.com/your-username/DiscordConnect4.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the necessary libraries installed, such as `discord.py`.

3. Set up a Discord bot and obtain the bot token. Refer to Discord's documentation on how to create and set up a bot.

4. Configure the bot token in `main.py`. Replace `'YOUR_BOT_TOKEN'` with your actual bot token.

5. Customize the welcome message, endgame message, and the initial game board in the respective text files (`welcome.txt`, `endgame.txt`, `newboard.txt`).

6. Run the `main.py` script to start the Discord bot and begin playing Connect 4 on Discord.

   ```bash
   python main.py
   ```

   Make sure your Discord bot is added to your server and has the necessary permissions.

7. Enjoy playing Connect

 4 with other users on Discord!

## Requirements

The following dependencies are required for the DiscordConnect4 project:

- discord.py
- Other dependencies specified in `requirements.txt`

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

Please ensure that you have the necessary dependencies installed before running the project.

Now, gather your friends, invite the DiscordConnect4 bot to your server, and have a fantastic time playing Connect 4 together!

Let the disc-dropping action begin! :game_die:
