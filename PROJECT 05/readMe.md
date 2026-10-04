# Game Project

## Project Structure

The game is divided into separate Python modules.

* `main.py` contains the main game program and controls the game flow.
* `player.py` contains the `Player` class.
* `room.py` contains the `Room` class.
* `item.py` contains the `Item` class.

## Classes

### Player

The Player class has:

* name
* age
* location
* apples
* keys
* diamonds
* sword status
* warrior status
* forest completion status

The player can:

* pick apples
* move between rooms
* collect keys
* escape from the Forest
* get a sword
* become a Warrior
* fight enemies
* collect diamonds

### Room

The Room class has:

* name
* description

The game contains four rooms:

* Village
* Cave
* Forest
* Palace

### Item

The Item class has:

* name

The game contains four items:

* Apple
* Key
* Sword
* Diamond

## Game Actions

The player can:

* pick apples in the Village
* go to the Cave
* collect available keys
* go to the Forest
* escape from the bears
* reach the Palace
* open the Palace door
* collect the sword
* become a Warrior
* fight enemies
* collect diamonds
* exit the game

## Game Rules

* The player must be older than 12 years to play the game.
* Each time the player picks apples, 100 apples are added.
* Every 100 apples makes one key available in the Cave.
* A maximum of 5 keys can be available in the Cave.
* The player must take a key from the Cave before going to the Forest.
* The Forest contains bears.
* After escaping from the Forest, the player reaches the Palace.
* The player can open the Palace door and get the sword.
* After getting the sword, the player becomes a Warrior.
* Each defeated enemy gives the player one diamond.
* The player wins after collecting 5 diamonds.

## Winning Condition

The player wins the game when 5 diamonds have been collected.
