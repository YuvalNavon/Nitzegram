import pygame

from Nitzagram.classes.TextPost import TextPost
from classes.ImagePost import ImagePost

from classes.Post import Post
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from helpers import screen
from helpers import mouse_in_button
from buttons import like_button, comment_button, click_post_button
from helpers import read_comment_from_user
from classes.Comment import Comment

def add_image (img_path , x_pos, y_pos , width , height):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x_pos, y_pos))


def main():
    post = ImagePost("images/Ramogus.jpeg.", "Wembley",
                "SIUUUUU")
    post2 = ImagePost("images/Ramogus2.jpeg.", "Me", "rabbittt :)")
    post3 = ImagePost("images/Ramogus3.jpeg", "Also Me", "rabbittt :))")
    post4 = ImagePost("images/Ramogus4.jpeg", "hi", "cute rabbit!!!!!!")
    post5 = ImagePost("images/img.png", "DAMN DANIEL", "AR AR AR")
    post6 = TextPost("Wassup", "Tkuma", "WASSAP my mate you good", (216,79,81), (74,144,205))
    post7 = TextPost("Hello Rom", "Nitzanim", "Enjoy Majora's Mask", (216,79,81), (74,144,205))


    post_list = [post, post2, post3, post4, post5, post6, post7]
    current_index = 0
    new_post = post_list[current_index]
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    # TODO (CLASS): set up background image(load and define size)
    img = pygame.image.load("Images/background.png")
    img = pygame.transform.scale(img , (WINDOW_WIDTH ,WINDOW_HEIGHT))
    screen.blit(img, (0,0))

    current_post = new_post

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, pos):
                    current_post.add_like()
                if mouse_in_button(comment_button, pos):
                    new_comment = read_comment_from_user()
                    comment = Comment(new_comment)
                    current_post.add_comment(comment)
                if mouse_in_button(click_post_button, pos):
                    if current_index == len(post_list) - 1:
                        current_index = 0
                    else:
                        current_index += 1
                    current_post = post_list[current_index]

                print(pos)

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        # TODO (CLASS): display the background image
        screen.blit(img, (0, 0))

        # TODO: Write the comment test here

        # TODO: call the test post here
        current_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()

main()