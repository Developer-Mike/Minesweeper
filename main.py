import pygame
import assets
from game import Game

field_count = (20, 20)
field_size = 40
fps = 30

pygame.init()
assets.init(field_size)
clock = pygame.time.Clock()

game = Game(field_count, field_size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif game.won is None:
            game.handle_event(event)

    game.render()

    if game.won is not None:
        print("was")
        pygame.draw.rect(pygame.display.set_mode((field_count[0] * field_size, field_count[1] * field_size)),
                         (0, 255, 0),
                         pygame.Rect(100, 100, 50, 50))

    pygame.display.update()
    clock.tick(fps)
