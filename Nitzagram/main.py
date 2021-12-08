import pygame

from classes.Button import Button
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from helpers import screen


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    # TODO (CLASS): set up background image(load and define size)
    img_path = "Images/background.png"
    image = pygame.image.load(img_path)
    image = pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(image, (0, 0))

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        # TODO (CLASS): display the background image

        # TODO: Write the comment test here

        # TODO: call the test post here

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()