from random import randint
import pygame


class Circle:
    def __init__(self, x, y, bound_y):
        self.x = x
        self.y = y
        self.r = 10
        self.v = 100
        self.bound_y = bound_y - self.r
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.clock = pygame.time.Clock()

    def draw(self, screen):
        self.move()
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.r)

    def move(self):
        if self.y < self.bound_y:
            self.y += self.v * self.clock.tick() / 1000
        self.y = self.bound_y if self.y > self.bound_y else self.y

