import arcade

class Button(arcade.Sprite):
    def __init__(self, f, h):
        super().__init__("data/buttons/" + f + ".png", center_x = 890, center_y = h*84 - 10)
        self.f = f
        self.type = "Button"

    def klick(self, field):
        if self.f == "add_village":
            field.add_village()
    
class Txt(arcade.Text):
    def __init__(self, txt, x, y, color, size, b = False):
        super().__init__(txt, x, y, color, font_name="data/fonts/minimalistic.ttf", font_size = size, bold = b)
        self.type = "Txt"

class Img(arcade.Sprite):
    def __init__(self, file, x, y):
        super().__init__(file, scale = 2, center_x = x, center_y = y)
        self.type = "Img"