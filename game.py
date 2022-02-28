import random
import numpy as np
import pygame
from field import Field


def flatten(array):
    return list(np.array(array).flatten())


class Game:
    def __init__(self, field_count, field_size):
        self.won = None
        self.field_count = field_count
        self.field_size = field_size

        self.fields = [[Field((x, y), field_size) for y in range(field_count[1])] for x in range(field_count[0])]
        for field in flatten(self.fields):
            field.set_bomb_neighbours(self.fields)
        self.uncover_first()

        self.surface = pygame.display.set_mode((field_count[0] * field_size, field_count[1] * field_size))

    def uncover_first(self):
        first_uncovered = False
        while not first_uncovered:
            random_field = self.fields[random.randint(0, self.field_count[0] - 1)][random.randint(0, self.field_count[1] - 1)]
            if not random_field.bomb and random_field.bombs_neighbour_count == 0:
                random_field.uncover(self.fields)
                first_uncovered = True

    def get_field_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        field_pos = int(mouse_pos[0] / self.field_size), int(mouse_pos[1] / self.field_size)
        return self.fields[field_pos[0]][field_pos[1]]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()

            if left:
                game_over = self.get_field_hover().uncover(self.fields)
                if game_over:
                    self.won = False

            if right:
                self.get_field_hover().tag()

    def render(self):
        all_fields_uncovered = True
        for field in flatten(self.fields):
            field.render(self.surface)

            if not field.uncovered and not field.bomb:
                all_fields_uncovered = False

        if all_fields_uncovered:
            self.won = True
