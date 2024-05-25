from config import *
import pygame
from pygame.locals import *
import pygame_gui
import requests
import io

class Game:
    def __init__(self) -> None:
        
        pygame.init()
        pygame.display.set_caption("Your Lovely Meme!")
        
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background.fill(PINK)
        
        r = requests.get(IMAGE_URL)
        img = io.BytesIO(r.content)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))


        self.text_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((WINDOW_WIDTH - 200, 20, 400, 100)), 
        manager=self.manager
        )
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.text = "Your Lovely Meme!"
        
    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                self.manager.process_events(event)
                
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        if event.ui_element == self.text_input:
                            self.text = event.text

            self.manager.update(time_delta)
            self.surface.blit(self.background, (0,0)) 
            self.surface.blit(self.image, (0, 0))  
            self.draw_text(self.text) 
            self.manager.draw_ui(self.surface) 

            pygame.display.flip()
        pygame.quit()

    def draw_text(self, text):
        font = pygame.font.Font(FONT, FONT_SIZE)
        rendered_text = font.render(text, True, PINK)  
        text_rect = rendered_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 15))
        self.surface.blit(rendered_text, text_rect)

if __name__ == "__main__":
    game = Game()
    game.run()
