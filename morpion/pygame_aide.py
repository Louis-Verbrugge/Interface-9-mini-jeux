from pygame import *

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

C1_GREEN = (204, 255, 204)
C1_BLUE = (153, 204, 255)
bgColor = C1_GREEN

size = width, height = 800, 600
screen = display.set_mode(size)
screen.fill(bgColor)

draw.rect(screen, RED, (50, 20, 150, 100))
draw.rect(screen, GREEN, (100, 70, 150, 100))

draw.rect(screen, RED, (450, 20, 150, 100), 1)
draw.rect(screen, GREEN, (500, 70, 150, 100), 5)

draw.ellipse(screen, RED, (50, 320, 150, 100))
draw.ellipse(screen, GREEN, (100, 370, 150, 100))

draw.ellipse(screen, RED, (450, 320, 150, 100), 1)
draw.ellipse(screen, GREEN, (500, 370, 150, 100), 5)

draw.line(screen, GRAY, (300,100), (500,500), 5)

# créer un triangle avec 3 lignes de code
draw.line(screen, BLACK, (350, 350), (450, 450), 3)
draw.line(screen, RED, (450, 450), (250, 450), 3)
draw.line(screen, GREEN, (250, 450), (350, 350), 3)

# créer un triangle avec 1 seule ligne de code
draw.lines(screen,BLUE,True, ((650,200),(750,300),(550,300)),5)

display.update()
init()

run = True
while run:
    for pyEvent in event.get():
        if pyEvent.type == QUIT:
            run = False

quit()