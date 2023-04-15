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

x = 20
y = 50

for filename in os.listdir(image_directory):
    if filename.endswith(".png"):
        path = os.path.join(image_directory, filename)
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, image_size)
        x += image_size[0] + 10
        if x > SCREEN_WIDTH:
            x = 50
            y += image_size[1] + 10
        # images[filename] = image
        images[image] = (x, y)

# Position and size of spirites
CARD_WIDTH = 100
CARD_HEIGHT = 150
CARD_PADDING = 20

# Original position
# CARD_X = SCREEN_WIDTH / 2 - CARD_WIDTH / 2
# CARD_Y = SCREEN_HEIGHT / 2 - CARD_HEIGHT / 2
CARD_X = 20
CARD_Y = 50

selected_image = None

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # マウスがクリックされたら、どの画像が選択されたかを判定する
            x, y = event.pos
            for image, position in images.items():
                image_width, image_height = image.get_size()
                rect = pygame.Rect(position[0], position[1], image_width, image_height)
                if rect.collidepoint(x, y):
                    selected_image = image
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            # マウスが離されたら、選択された画像の位置を更新する
            if selected_image:
                x, y = event.pos
                images[selected_image] = (x, y)
                selected_image = None
        elif event.type == pygame.MOUSEMOTION:
            # マウスがドラッグされているとき、選択された画像を移動する
            if selected_image:
                x, y = event.pos
                images[selected_image] = (x, y)

    # Displaying background
    screen.fill((0, 128, 0))

    for image, position in images.items():
        screen.blit(image, position)

    # # Displaying spirites
    # screen.blit(card_1_image, (CARD_X + CARD_WIDTH + CARD_PADDING, CARD_Y))
    # screen.blit(card_2_image, (CARD_X + CARD_WIDTH * 2 + CARD_PADDING * 2, CARD_Y))
    # screen.blit(card_3_image, (CARD_X + CARD_WIDTH * 3 + CARD_PADDING * 3, CARD_Y))
    # screen.blit(card_4_image, (CARD_X + CARD_WIDTH * 4 + CARD_PADDING * 4, CARD_Y))

    # Updating screen
    pygame.display.update()

# Finishing process
pygame.quit()