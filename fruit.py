class Fruit:
    def __init__(self, taste, color):
        self.taste = taste
        self.color = color 

    def ripeness(self):
        return self.color != "green"