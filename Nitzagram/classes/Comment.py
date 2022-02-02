from Nitzagram.classes.Post import *
from Nitzagram.constants import *


class Comment():

    def __init__(self, text):
        self.text = text

    def display(self, comment_num):
        font_name = "chalkduster.ttf"
        text_size = 15
        color = (0,0,0)
        x_pos= FIRST_COMMENT_X_POS
        y_pos = FIRST_COMMENT_Y_POS + (comment_num*COMMENT_LINE_HEIGHT)

        font = pygame.font.SysFont(font_name, text_size)
        screen.blit(font.render(self.text, True, color), (x_pos, y_pos))