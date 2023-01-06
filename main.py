import websockets as ws
import pygame
from pygame.locals import *
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()
pygame.init()

PORT = 8080

PC = {
    'gaming': os.getenv("GAMING_PC")
}


class PC_Button:
    WIDTH, HEIGHT = 500, 300

    def __init__(self, screen, position, text, address):
        self.screen = screen
        self.position = position
        self.text = text
        self.address = address
        self.rect = pygame.Rect(self.position[0], self.position[1], self.WIDTH, self.HEIGHT)
        self.draw()

    def locatedIn(self, position):
        left = self.position[0]
        right = left + self.WIDTH
        top = position[1]
        bottom = top + self.HEIGHT
        return left <= position[0] <= right and top <= position[1] <= bottom

    def draw(self):
        pygame.draw.rect(self.screen, (100, 100, 100), self.rect)


def main():
    print(PC['gaming'])

    active = True
    screen = pygame.display.set_mode()

    buttons = [
        PC_Button(screen, (100, 300), "Gaming PC", PC['gaming']),
        PC_Button(screen, (700, 300), "Living Room PC", PC['gaming']),
        PC_Button(screen, (1300, 300), "Laptop", PC['gaming'])
        ]

    pygame.display.update()

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    active = False
    pygame.quit()


if __name__ == '__main__':
    main()
