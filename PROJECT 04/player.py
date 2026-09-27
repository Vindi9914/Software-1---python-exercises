class Player:
    def __init__(self, name, location):
        self.name = name
        self.items = []
        self.location = location

    def move(self, destination):
        self.location = destination
        print("You moved to", destination.name)

    def collect_item(self):
        if self.location.item is not None:
            item = self.location.item
            self.items.append(item)
            self.location.item = None
            print(item.name, "has been added to your inventory.")
        else:
            print("There is no item here.")