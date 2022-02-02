import pygame
from Nitzagram.helpers import screen
from Nitzagram.classes.Post import Post
from Nitzagram.constants import *
class ImagePost(Post):
    def __init__(self, image_src, location, description):
        Post.__init__(self, location, description)
        image = pygame.image.load(image_src)
        image = pygame.transform.scale(image, (POST_WIDTH,POST_HEIGHT))
        self.image = image

    def display_content(self):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))

