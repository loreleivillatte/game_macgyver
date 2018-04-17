"""class level, Player"""

import pygame

from pygame.locals import *

from constants import *


class Level:
    """create labyrinth"""
    def __init__(self, file):
        """use file .txt"""
        self.file = "level.txt"
        self.frame = 0

    def generate(self):
        """generate level of labyrinth,
        create a general list, containing a list per line to display"""
        with open(self.file) as file:
            frame_level = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                frame_level.append(line_level)
            self.frame = frame_level

    def display(self, screen):
        """display level depends on structure of list returned by generate"""
        wall = pygame.image.load("pictures/wall.png").convert()
        end = pygame.image.load("pictures/guard.png").convert_alpha()
        num_line = 0
        for line in self.frame:
            num_case = 0
            for sprite in line:
                sprite_x = num_case * sprite_size
                sprite_y = num_line * sprite_size
                if sprite == 'w':
                    screen.blit(wall, (sprite_x, sprite_y))
                elif sprite == "e":
                    screen.blit(end, (sprite_x, sprite_y))
                num_case += 1
            num_line += 1


class Player:
    """character"""
    def __init__(self, down, left, right, up, level):
        self.down = pygame.image.load(down).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.right = pygame.image.load(right).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        """starting position of the character"""
        self.case_x = 7
        self.case_y = 2
        self.x = 7 * 40
        self.y = 2 * 40
        self.direction = self.down
        self.level = level
        
    def update(self, direction):
        """ moving the character"""
        if direction == 'down':
            if self.case_y < (nb_sprites - 1):
                """ can't walk on wall"""
                if self.level.structure[self.case_y+1][self.case_x] != 'w':
                    self.case_y += 1
                    self.y = self.case_y * sprite_size
            self.direction = self.down
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'w':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size
            self.direction = self.left
        if direction == 'right':
            if self.case_x < (nb_sprites - 1):
                if self.level.structure[self.case_y][self.case_x+1] != 'w':
                    self.case_x += 1
                    self.x = self.case_x * sprite_size
            self.direction = self.right
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'w':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size
            self.direction = self.up