import pygame

from Nitzagram.helpers import screen, center_text
from Nitzagram.classes.Post import Post
from Nitzagram.helpers import  from_text_to_array
from Nitzagram.constants import *

class TextPost(Post):
    def __init__(self, location, description,  text, text_color, background_color ):
        Post.__init__(self, location, description)
        self.background_color = background_color
        self.text_array = from_text_to_array(text)
        self.text_color = text_color


    def display_content(self):
        pygame.draw.rect(screen, self.background_color, pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))
        font_name = "chalkduster.ttf"
        font = pygame.font.SysFont(font_name, TEXT_POST_FONT_SIZE)
        row_number = 0
        for text in self.text_array:
            texti = font.render(text, True, self.text_color)
            screen.blit(texti, center_text(len(self.text_array), texti, row_number))
            row_number = row_number + 1


