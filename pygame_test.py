import pygame
import os

# Initialization
pygame.init()

# Setting up game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test Game")

# Reading image files and resize
# reading all images in a specific directory instead of selecting one by one
image_directory = "images"
image_size = (140, 200)
images = {}

for filename in os.listdir(image_directory):
    if filename.endswith(".png"):
        path = os.path.join(image_directory, filename)
        image = pygame.image.load(path)
        print(image.get_size())
        image = pygame.transform.scale(image, image_size)
        images[filename] = image
        print(images)

# # Reading image file
# card_1_image = pygame.image.load(".\images\A of Spade.png")
# card_2_image = pygame.image.load(".\images\A of Heart.png")
# card_3_image = pygame.image.load(".\images\A of Club.png")
# card_4_image = pygame.image.load(".\images\A of Diamond.png")
# image1_width, image1_height = card_1_image.get_size()
# image2_width, image2_height = card_2_image.get_size()
# image3_width, image3_height = card_3_image.get_size()
# image4_width, image4_height = card_4_image.get_size()
# card_1_image = pygame.transform.scale(card_1_image, (image1_width // 6, image1_height // 6))
# card_2_image = pygame.transform.scale(card_2_image, (image2_width // 6, image2_height // 6))
# card_3_image = pygame.transform.scale(card_3_image, (image3_width // 6, image3_height // 6))
# card_4_image = pygame.transform.scale(card_4_image, (image4_width // 6, image4_height // 6))

# Position and size of spirites
CARD_WIDTH = 100
CARD_HEIGHT = 150
CARD_PADDING = 20

# Original position
# CARD_X = SCREEN_WIDTH / 2 - CARD_WIDTH / 2
# CARD_Y = SCREEN_HEIGHT / 2 - CARD_HEIGHT / 2
CARD_X = 20
CARD_Y = 50

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Displaying background
    screen.fill((0, 128, 0))

    x = 20
    y = 50
    for filename, image in images.items():
        screen.blit(image, (x, y))
        x += image_size[0] + 10
        if x > SCREEN_WIDTH:
            x = 50
            y += image_size[1] + 10

    # # Displaying spirites
    # screen.blit(card_1_image, (CARD_X + CARD_WIDTH + CARD_PADDING, CARD_Y))
    # screen.blit(card_2_image, (CARD_X + CARD_WIDTH * 2 + CARD_PADDING * 2, CARD_Y))
    # screen.blit(card_3_image, (CARD_X + CARD_WIDTH * 3 + CARD_PADDING * 3, CARD_Y))
    # screen.blit(card_4_image, (CARD_X + CARD_WIDTH * 4 + CARD_PADDING * 4, CARD_Y))

    # Updating screen
    pygame.display.update()

# Finishing process
pygame.quit()