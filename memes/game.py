from config import *
import pygame
from pygame.locals import *
import time

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        pygame.display.set_caption("Meme Generator")
        self.surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.surface.fill(WHITE)

    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            font = pygame.font.Font(FONT, FONT_SIZE)
            text = font.render('Hello TechWise', True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            self.surface.blit(text, text_rect)
            pygame.display.flip()
            time.sleep(SLEEP_TIME)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
