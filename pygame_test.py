import pygame

# Initialization
pygame.init()

# Setting up game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test Game")

# Reading image file
# card_back_image = pygame.image.load("card_back.png")
card_1_image = pygame.image.load(".\images\A of Spade.png")
card_2_image = pygame.image.load(".\images\A of Heart.png")
card_3_image = pygame.image.load(".\images\A of Club.png")
card_4_image = pygame.image.load(".\images\A of Diamond.png")

# Position and size of spirites
CARD_WIDTH = 100
CARD_HEIGHT = 150
CARD_PADDING = 20

# Original position
# CARD_X = SCREEN_WIDTH / 2 - CARD_WIDTH / 2
# CARD_Y = SCREEN_HEIGHT / 2 - CARD_HEIGHT / 2
CARD_X = 50
CARD_Y = 50

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Displaying background
    screen.fill((0, 128, 0))

    # Displaying spirites
    # screen.blit(card_back_image, (CARD_X, CARD_Y))
    screen.blit(card_1_image, (CARD_X + CARD_WIDTH + CARD_PADDING, CARD_Y))
    screen.blit(card_2_image, (CARD_X + CARD_WIDTH * 2 + CARD_PADDING * 2, CARD_Y))
    screen.blit(card_3_image, (CARD_X + CARD_WIDTH * 3 + CARD_PADDING * 3, CARD_Y))
    screen.blit(card_4_image, (CARD_X + CARD_WIDTH * 4 + CARD_PADDING * 4, CARD_Y))

    # Updating screen
    pygame.display.update()

# Finishing process
pygame.quit()