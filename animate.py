import random
from coctail import coctail_sort
from bogo import bogo_sort
from buble import buble_sort
from exchange import exchange_sort
from brick import brick_sort
from comb import comb_sort
from gnome import gnome_sort
from insertion import insertion_sort
from shell import shell_sort
from binary import binary_sort
from selection import selection_sort
from heap import heap_sort
import pygame

#global variable
width = 600
height = 400
n = 50
speed = 10
OPEN_SANS = "./FreeSansBold.ttf"

COLORS = {
    "background" : (35, 35, 40),
    "regular" : (255,248,240),
    "highlight1" : (239,71,111),
    "highlight2" : (255,209,102),
    "highlight3" : (17,138,178),
    "sorted" : (6,215,160)
}

ALGORITHMS = {
    "Bogo Sort" : bogo_sort,
    "Buble Sort" : buble_sort,
    "Brick Sort" : brick_sort,
    "Comb Sort" : comb_sort,
    "Cocktail Sort" : coctail_sort,
    "Exchange Sort" : exchange_sort,
    "Gnome Sort" : gnome_sort,
    "Insertion Sort" : insertion_sort,
    "Shell Sort" : shell_sort,
    "Binary Sort" : binary_sort,
    "Selection Sort" : selection_sort,
    "Heap Sort" : heap_sort
}

#draw single bar
def draw_bar(array, i, screen, color):
    n = len(array)
    w, h = screen.get_size()
    bar_width = w // n
    bar_height = h // n * array[i]
    x = bar_width * i
    y = h - bar_height
    bar = pygame.Rect(x,y,bar_width,bar_height)
    pygame.draw.rect(screen,color,bar)

#function to visualize array
def draw_bars(array, screen, highlight1=[],highlight2=[],highlight3=[], sorted=False):
    screen.fill(COLORS["background"])
    n = len(array)
    if sorted:
        for i in range(n):
            draw_bar(array, i, screen, COLORS["sorted"])

    else:
        for i in range(n):
            draw_bar(array, i, screen, COLORS["regular"])
        for i in highlight1:
            draw_bar(array, i, screen, COLORS["highlight1"])
        for i in highlight2:
            draw_bar(array, i, screen, COLORS["highlight2"])
        for i in highlight3:
            draw_bar(array, i, screen, COLORS["highlight3"])

#animation function
def animate(name, n =  50, speed = 10, width = 1000, height = 500, **kwargs):

    #get algorithm from dictionary
    algorithm = ALGORITHMS[name]
    print(algorithm)

    # create array and sorting process generator
    array = random.sample(range(1,n+1),n)
    process = algorithm(array, **kwargs)

    #initial pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((width,height))

    #window caption
    pygame.display.set_caption("Sorting algorithm visualization")

    #text box with algorithm name
    font = pygame.font.Font(OPEN_SANS, 32)
    text = font.render(name, True, COLORS["regular"], COLORS["background"])
    textbox = text.get_rect(topleft = (10,10))

    #animation loop
    animating = True
    pausing = False
    while animating:

        if not pausing :

            # next step in the sorting process
            array, hl1, hl2, hl3 = next(process,(None, None, None, None))

            # bart chart visualization
            if array is not None:
                draw_bars(array, screen, hl1,hl2,hl3)
            else:
                array=list(range(1, n+1))
                draw_bars(array, screen, sorted=True)

            #add text box
            screen.blit(text, textbox)

            # update screen
            pygame.display.flip()

            # pause
            pygame.time.wait(1000 // speed)

            # track user interaction
        for event in pygame.event.get():
            # user closes
            if event.type == pygame.QUIT:
                animating = False

            if event.type == pygame.KEYDOWN:
                #left arrow key decrease animation speed
                if event.key == pygame.K_LEFT:
                    speed = max(1, speed - 1)

                #right arrow key increase animation speed
                if event.key == pygame.K_RIGHT:
                    speed = min(100, speed + 1)

                #pausing space bar
                if event.key == pygame.K_SPACE:
                    pausing = not pausing

                #reshuffle array by press enter
                if event.key == pygame.K_RETURN:
                    array = random.sample(range(1,n+1),n)
                    process = algorithm(array, **kwargs)
                    pausing = False

                # escape key to terminate animation
                if event.key == pygame.K_ESCAPE:
                    animating = False

