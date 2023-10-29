import arcade

class Button(arcade.Sprite):
    def __init__(self, f, h):
        super().__init__("data/buttons/" + f + ".png", center_x = 890, center_y = h*84)
        self.f = f
        self.type = "Button"

    def klick(self, field):
        if self.f == "add_village":
            field.add_village()
    
class Txt(arcade.Text):
    def __init__(self, txt, x, y, color, size):
        super().__init__(txt, x, y, color, size)
        self.type = "Txt"