
class Room:
    """Represent a place in the adventure with a name and description."""

    def __init__(self, name, description):
        self.name = name
        self.description = description


village = Room(
    "Village",
    "A quiet village where you can collect apples and prepare for your journey."
)

cave = Room(
    "Cave",
    "A cave where keys become available when you collect apples in the Village."
)

forest = Room(
    "Forest",
    "A forest path where you must escape from bears to reach the Palace."
)

meadow = Room(
    "Meadow",
    "A meadow path where you must escape from snakes to reach the Palace."
)

palace = Room(
    "Palace",
    "A locked palace where the player can find a sword and fight enemies to collect diamonds."
)
