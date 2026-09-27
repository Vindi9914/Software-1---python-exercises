# Game Project

## Project Structure

The game is divided into separate Python modules.

- `main.py` contains the main game program and menu.
- `player.py` contains the Player class.
- `room.py` contains the Room class.
- `item.py` contains the Item class.

## Classes

### Player

The Player class has:
- name
- items
- location

The player can:
- move to another room
- collect an item

### Room

The Room class has:
- name
- item

A room can contain one item.

### Item

The Item class has:
- name
- weight

## Game Actions

The player can:
- explore the current room
- move to another room
- collect an item
- check the inventory
- exit the game