class Flower:
    def __init__(self, color, is_blooming = False, produces_fruit = False):
        self.color = color
        self.is_blooming = is_blooming
        self.produces_fruit = produces_fruit

    def smell(self):
        print("I'm not sure if this flower has a smell.")

    def neighbor(self, neighbor):
        print(f"The flower next to me is {neighbor.color}")


# flower1 = Flower("purple", True, False)
# flower2 = Flower("Pink", True, True)
# # print(f"The flower's color is {flower1.color}.")
# flower1.smell()
# flower2.smell()
# flower1.neighbor(flower2)