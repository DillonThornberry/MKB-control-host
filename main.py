import pygame
from pygame.locals import *
from dotenv import load_dotenv
import os
from WS_Client import WS_Client
from time import sleep

load_dotenv()
pygame.init()

PC = {
    'gaming': os.getenv("GAMING_PC")
}


class PC_Button:
    WIDTH, HEIGHT = 500, 300
    FONT = pygame.font.Font('freesansbold.ttf', 48)

    def __init__(self, screen, position, text, address):
        self.screen = screen
        self.position = position
        self.caption = text
        self.address = address
        self.rect = pygame.Rect(self.position[0], self.position[1], self.WIDTH, self.HEIGHT)
        self.text = self.FONT.render(self.caption, True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.rect.x + self.WIDTH //2, self.rect.y + self.HEIGHT // 2)
        self.draw()

    def locatedIn(self, position):
        left = self.rect.x
        right = left + self.WIDTH
        top = self.rect.y
        bottom = top + self.HEIGHT
        return left <= position[0] <= right and top <= position[1] <= bottom

    def draw(self):
        pygame.draw.rect(self.screen, (100, 100, 100), self.rect)
        self.screen.blit(self.text, self.textRect)


def main():
    print(PC['gaming'])

    active = True
    screen = pygame.display.set_mode()

    labelFont = pygame.font.Font('freesansbold.ttf', 72)
    labelText = labelFont.render("Select a PC to control", True, (200, 200, 200))
    labelRect = labelText.get_rect()
    labelRect.center = (screen.get_rect().width // 2, screen.get_rect().height // 4)
    screen.blit(labelText, labelRect)

    buttons = [
        PC_Button(screen, (100, 450), "Gaming PC", PC['gaming']),
        PC_Button(screen, (700, 450), "Living Room PC", PC['gaming']),
        PC_Button(screen, (1300, 450), "Laptop", PC['gaming'])
        ]

    pygame.display.update()
    UI_mode = True
    ws_client = None

    while active:
        for event in pygame.event.get():
            if UI_mode:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        active = False
                    elif event.key == K_x and pygame.key.get_mods() & KMOD_ALT:
                        print('alt+x')

                elif event.type == MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.locatedIn(pygame.mouse.get_pos()):
                            print(button.caption)
                            UI_mode = False
                            client = WS_Client(button.address)
            else:
                if event.type == KEYDOWN:
                    if event.key == K_x and pygame.key.get_mods() & KMOD_ALT:
                        active = False

    pygame.quit()


if __name__ == '__main__':
    main()
