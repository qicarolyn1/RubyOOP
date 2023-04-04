from Flower import Flower

class FruitBearingFlower(Flower):
    def __init__(self, flower_color, fruit_type, fruit_count):
        super().__init__(color = flower_color, is_blooming = True, produces_fruit = True)
        self.fruit_type = fruit_type
        self.fruit_count = fruit_count

    def smell(self):
        print("This flower smells nice.")
        super().smell()

    def pick_fruit(self):
        self.fruit_count -= 1
        print(f"We currently have this much fruit: {self.fruit_count}")

