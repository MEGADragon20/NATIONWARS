import arcade

SCREENWIDTH  = 1000
SCREENHEIGHT = 840

class StartScreen(arcade.View):
    def __init__(self):
        self.done = False
        super().__init__()
        self.names = ""

    def on_draw(self):
        if self.done:
            raise
        arcade.start_render()
        arcade.draw_text("NationWars", SCREENWIDTH/2, SCREENHEIGHT/2 + 100,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Players:", SCREENWIDTH/2, SCREENHEIGHT/2,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text(self.names, SCREENWIDTH/2, SCREENHEIGHT/2 - 50,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Start Game", SCREENWIDTH/2, SCREENHEIGHT/2 - 150,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.BACKSPACE and len(self.names) > 0:
            self.names = self.names[:-1]
        elif key == arcade.key.ENTER:
            print("Start game with player name:", list(filter(lambda x: x.strip(), self.names.split(","))))

    def on_text(self, text):
        self.names += text if text != "\n" and text != "\r" else ""

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        start_text_x = SCREENWIDTH/2
        start_text_y = SCREENHEIGHT/2 - 150
        start_text_width = 200  # Approximate width of the text
        start_text_height = 30  # Height of the text

        # Check if the click is within the bounds of the text
        if start_text_x - start_text_width/2 <= x <= start_text_x + start_text_width/2 and \
        start_text_y - start_text_height/2 <= y <= start_text_y + start_text_height/2:
            print("Start game with player name:", list(filter(lambda x: x.strip(), self.names.split(","))))
            self.done = True

        return super().on_mouse_release(x, y, button, modifiers)

def main():
    window = arcade.Window(SCREENWIDTH, SCREENHEIGHT, "NationWars Start Screen")
    start_view = StartScreen()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()