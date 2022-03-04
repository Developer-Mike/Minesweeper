import time

import pygame
import assets
from game import Game

field_count = (20, 20)
field_size = 40
game_over_window_size = (500, 300)
fps = 30

pygame.init()
assets.init(game_over_window_size, field_size)
clock = pygame.time.Clock()
surface = pygame.display.set_mode((field_count[0] * field_size, field_count[1] * field_size + field_size))

game = Game(surface, field_count, field_size)
while True:
    if game.won is not None:
        clock.tick(1)
        game = Game(surface, field_count, field_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif game.won is None:
            game.handle_event(event)

    game.render()

    pygame.display.update()
    clock.tick(fps)

    if game.won is None:
        game.time += 1 / float(fps)
