class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description


village = Room("Village", "You can pick apples here.")

cave = Room("Cave", "You can find keys here.")

forest = Room("Forest", "There are bears in the forest.")

palace = Room("Palace", "You can open the palace door here.")