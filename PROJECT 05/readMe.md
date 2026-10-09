# Guardians of the Green World

## Game Idea

Guardians of the Green World is a text-based adventure game written in Python. The player begins in a village, travels through a cave, and chooses one of two routes: the Forest Path or the Meadow Path. Both routes lead to a Palace where the player can find a sword, become a Warrior, and fight enemies and save the world.



## Objective

The main objective is to reach the Palace, obtain the sword, defeat enemies, and collect five diamonds. The player wins after collecting five diamonds.

To reach the Palace safely, the player must choose how to escape from a bear on the Forest Path or a snake on the Meadow Path.

## How the Game Works

1. The player enters a name and age.
2. If a saved game exists for that name, the player can choose to continue it.
3. The player starts in the Village and collects apples.
4. Each apple-picking action adds 100 apples and makes a key available in the Cave, up to a maximum of five keys.
5. The player takes a key in the Cave and chooses the Forest Path or Meadow Path.
6. On the Forest Path, the player encounters a bear and must choose a safe way to escape.
7. On the Meadow Path, the player encounters a snake and must choose a safe way to move away.
8. After successfully escaping, the player can continue to the Palace.
9. At the Palace, the player uses the key to open the door and obtain a sword.
10. The player becomes a Warrior and can fight enemies. Each defeated enemy gives one diamond.
11. The player wins after collecting five diamonds.
12. The player can save progress and exit, then load the saved game later.

## Alternative Routes

The game offers two routes from the Cave to the Palace:

* **Forest Path:** The player encounters a bear. Choosing to escape quietly through the trees allows the player to continue to the Palace. Trying to run past the bear does not succeed.
* **Meadow Path:** The player encounters a snake. Slowly moving away from the snake allows the player to continue to the Palace. Trying to step past the snake does not succeed.

The player can return to the Cave from either route. Before obtaining the sword, the player can also return from the Palace to either path.

Both routes offer different challenges but lead toward the same main objective.

## Functionalities

* Command-line interface with menus and a main game loop.
* Player name and age input.
* Age restriction for players aged 13 and over.
* Separate `Player`, `Room`, and `Item` classes.
* Four item types: apple, key, sword, and diamond.
* Five locations: Village, Cave, Forest, Meadow, and Palace.
* Two alternative routes with different animal encounters.
* Choices that determine whether the player can escape an animal.
* Player status display.
* Saving and loading player progress using `savegame.txt`.
* Winning condition based on collecting five diamonds.
* Input validation for menu choices.


## Age Rating

The game is intended for players aged **13 and over**. Players aged 12 or younger cannot continue past the age check.

## Project Structure

* `main.py` - controls the menus, game loop, routes, rules, and save/load functions.
* `player.py` - defines the `Player` class and stores the player's progress.
* `room.py` - defines the `Room` class and the locations.
* `item.py` - defines the `Item` class and the game's items.
* `intro.txt` - contains the story introduction.
* `instructions.txt` - explains how to play.
* `savegame.txt` - stores the current saved game when the game is played.
* `main_backup.py` - backup copy of the original main game file, if retained.


## Comments and Code Structure

The code is organised into classes, functions, and clearly labelled sections to keep related tasks together. Comments explain important parts of the program, including file handling, the main game loop, route choices, and the winning condition.

## Saving and Loading

Choose **Save and Exit** from a menu to save the player's progress. When starting the game again, enter the same player name and choose `yes` to continue the saved game.

The `savegame.txt` file is generated while playing. It contains player-specific progress and should not normally be committed to a public repository.
