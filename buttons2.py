import arcade
print(arcade.window_commands.get_display_size())
width, height = arcade.window_commands.get_display_size()
cartogrpah = 0
if 1152 > height >= 768:
    cartogrpah = 24
elif 1536 > height >= 1152:
    cartogrpah = 36
elif 2048 > height >= 1536:
    cartogrpah = 48
elif 2560 > height >= 2048:
    cartogrpah = 64

class Button(arcade.Sprite):
    def __init__(self, f, h: tuple):
        super().__init__("data/buttons/" + f + ".png", center_x = 20 + h[0]*84 + cartogrpah*32, center_y = h[1]*84 - 10)
        self.f = f
        self.type = "Button"

    def klick(self, field):
        if self.f == "add_village":
            field.add_village()
    
class Txt(arcade.Text):
    def __init__(self, txt, x, y, color, size, b = False):
        super().__init__(txt, 20 + cartogrpah*32 + x, y, color, font_name="data/fonts/minimalistic.ttf", font_size = size, bold = b)
        self.type = "Txt"

class Img(arcade.Sprite):
    def __init__(self, file, x, y):
        super().__init__(file, scale = 2, center_x = x, center_y = y)
        self.type = "Img"

class Num(arcade.Text):
    def __init__(self, txt, x, y, color, size, b = False):
        super().__init__(txt, x, y, color, font_name="data/fonts/minimalistic.ttf", font_size = size, bold = b)
        self.type = "Txt"