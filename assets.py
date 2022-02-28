import pygame

HIDDEN = pygame.image.load("assets/hidden.png")
UNCOVERED = pygame.image.load("assets/uncovered.png")
FLAG = pygame.image.load("assets/flag.png")
MINE = pygame.image.load("assets/mine.png")
NUMBERS = [pygame.image.load(f"assets/{i}.png") for i in range(1, 9)]


def init(field_size):
    global HIDDEN, UNCOVERED, FLAG, MINE, NUMBERS
    HIDDEN = pygame.transform.scale(HIDDEN, (field_size, field_size))
    UNCOVERED = pygame.transform.scale(UNCOVERED, (field_size, field_size))
    FLAG = pygame.transform.scale(FLAG, (field_size, field_size))
    MINE = pygame.transform.scale(MINE, (field_size, field_size))

    for i in range(len(NUMBERS) - 1):
        NUMBERS[i] = pygame.transform.scale(NUMBERS[i], (field_size, field_size))

