import pygame
from Nitzagram.constants import NUM_OF_COMMENTS_TO_DISPLAY, COMMENT_TEXT_SIZE, \
    VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS, POST_WIDTH, POST_HEIGHT, POST_X_POS, POST_Y_POS, \
    LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS, DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS, LIKE_TEXT_X_POS, \
    LIKE_TEXT_Y_POS, USER_NAME_X_POS, USER_NAME_Y_POS
from Nitzagram.helpers import screen

class Post:
    user_name = "Yuval"
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, location, description):
        """TODO write your code here"""
        self.description = description
        self.location = location
        self.counter_likes = 0
        self.comments = []
        self.comments_display_index = 0


    # Display image, description, location, likes and comments
    def display(self):
        """TODO write your code here"""
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()


    # Display Image
    def display_content(self):
        # Display the main picture
        """TODO write your code here"""
        pass

    # Display header : location and description
    def display_header(self):

        # display the location
        """TODO write your code here"""
        color = (50, 50, 50)
        font = pygame.font.SysFont("chalkduster.ttf", 15)
        screen.blit(font.render(Post.user_name, True, color),
                    (USER_NAME_X_POS, USER_NAME_Y_POS))

        font_location = 'chalkduster.ttf'
        text_size = 15
        color = (134, 134, 134)
        font = pygame.font.SysFont(font_location, text_size)
        screen.blit(font.render(self.location, True, color),
                    (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        # display description
        """TODO write your code here"""
        color = (50, 50, 50)
        screen.blit(font.render(self.description, True, color),
                    (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))


    def display_likes(self):
        """TODO write your code here"""
        font_likes = 'chalkduster.ttf'
        text_size = 15
        color = (134, 134, 134)
        likes_text = "Liked by " + str(self.counter_likes) + " users"
        font = pygame.font.SysFont(font_likes, text_size)
        screen.blit(font.render(likes_text, True, color),
                    (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

    def add_comment(self, new_comment):
        self.comments.append(new_comment)

    def add_like(self):
        self.counter_likes += 1


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            comment_to_display = comment_font.render("view more comments",
                                                     True, (134, 134, 134))
            screen.blit(comment_to_display, (VIEW_MORE_COMMENTS_X_POS,
                                             VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break