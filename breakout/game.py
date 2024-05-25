from config import *
import pygame
from pygame.locals import *
import time

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        pygame.display.set_caption("Breakout")
        self.surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.surface.fill(WHITE)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        print("the up key has been pressed down")
            pygame.display.flip()
            time.sleep(SLEEP_TIME)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
