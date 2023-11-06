import pygame

eingabe = input("Name: ")

class Pixel:
    def __init__(self, color):
        self.color = color
    
    def __str__(self) -> str:
        (r,g,b) = self.color
        return str(r) + "/" + str(g) + "/" + str(b)

SIZE = 1000, 800

pygame.init()
screen = pygame.display.set_mode(SIZE)

pixels = []
for i in range(24*24):
    pixels.append(Pixel((80, 200, 80)))


activecolor = (80, 200, 80)
painting = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // 25
            row = event.pos[1] // 25
            if 0 <= col < 24 and 0 <= row < 24:
                painting = True
                index = col + row * 24
                new_px = Pixel(activecolor)
                pixels[index] = new_px 
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_1:
                (r, b, g) = activecolor
                activecolor = (80, 200, 80)
            elif event.key == pygame.K_2:
                (r, b, g) = activecolor
                activecolor = (122, 122, 122)
            elif event.key == pygame.K_3:
                (r, b, g) = activecolor
                activecolor = (0, 0, 255)
            elif event.key == pygame.K_4:
                (r, b, g) = activecolor
                activecolor = (0, 80, 0)
        elif event.type == pygame.MOUSEMOTION:
            if painting:
                col = event.pos[0] // 25
                row = event.pos[1] // 25
                if 0 <= col < 24 and 0 <= row < 24:
                    index = col + row * 24
                    new_px = Pixel(activecolor)
                    pixels[index] = new_px
        elif event.type == pygame.MOUSEBUTTONUP:
            painting = False

    screen.fill((100, 100, 100))
    for i in range(len(pixels)):
        col = i % 24
        row = i // 24
        rect = pygame.Rect(col * 25, row * 25, 25, 25)
        pygame.draw.rect(screen, pixels[i].color, rect)
    pygame.draw.rect(screen, activecolor, pygame.Rect(620,20, 50,50) )
    pygame.display.flip()
pygame.quit()

file = []

for i in pixels:
    if i.color == (80, 200, 80):
        file.append("grass")
    elif i.color == (122, 122, 122):
        file.append("mountain")
    elif i.color == (0, 0, 255):
        file.append("water")
    elif i.color == (0, 80, 0):
        file.append("forest")

file.reverse()

with open(f'data\worlds/' + eingabe + '.csv', "x") as f:
    for i in file:
        f.write(str(i) + "\n")