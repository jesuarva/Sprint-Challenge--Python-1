import pygame  # TODO:  Fix intellisense
import random
import math

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 600]
BACKGROUND_COLOR = [255, 255, 255]

BRICKS = []
BRICKS_WIDTH = 40
BRICKS_HEIGHT = 20
BRICKS_PADDING_X = 5
BRICKS_PADDING_Y = 5
BRICKS_COLUMNS = math.floor(
    ((SCREEN_SIZE[0] - BRICKS_PADDING_X) / (BRICKS_WIDTH + BRICKS_PADDING_X)))
BRICKS_ROWS = math.floor(
    ((SCREEN_SIZE[1] / 2) / (BRICKS_HEIGHT + BRICKS_PADDING_Y)))


def debug_create_objects(object_list):

    kinetic = GameBall(1, object_list, SCREEN_SIZE,
                       Vector2(random.randint(
                           20, SCREEN_SIZE[0] - 20), SCREEN_SIZE[1] * 3/5),
                       Vector2(4*random.random() * -1, 4*random.random() * -1),
                       [255, 10, 0], 10)
    object_list.append(kinetic)

    block = KineticBlock(
        Vector2(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1]), 90, 21, [0, 0, 255])
    object_list.append(block)

    createBricksMatrix(object_list)


def createBricksMatrix(object_list):
    print('BRICKS_ROWS', BRICKS_ROWS)
    print('BRICKS_COLUMNS', BRICKS_COLUMNS)

    for r in range(BRICKS_ROWS):
        BRICKS.append([])
        # print(BRICKS)
        for c in range(BRICKS_COLUMNS):
            BRICKS[r].append([])
            BRICKS[r][c] = Brick(
                Vector2(BRICKS_PADDING_X + (c * (BRICKS_WIDTH + BRICKS_PADDING_X)), BRICKS_PADDING_Y + (r * (BRICKS_HEIGHT + BRICKS_PADDING_Y))), BRICKS_WIDTH, BRICKS_HEIGHT, [0, 0, 255])
            object_list.append(BRICKS[r][c])
        print('\n\n Row number:', r, 'colums in row:', c, '\n', BRICKS[r])


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy
    paddle = None
    mainBall = None

    while True:  # TODO:  Create more elegant condition for loop
        left = False
        right = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:  # TODO:  Get working
                if event.key == pygame.K_SPACE:
                    # TODO: Add behavior when button pressed
                    print(event)
                if event.key == pygame.K_s:
                    debug_create_objects(object_list)
                    for i in range(len(object_list)):
                        print(i, object_list[i])
                    mainBall = object_list[0]
                    paddle = object_list[1]
                    print('paddle', paddle, 'mainBall', mainBall.lives)
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_RIGHT:
                    print("\nRight pressed")
                    print(object_list[0].position.x)
                    paddle.movePaddle('RIGHT', SCREEN_SIZE[0])
                if event.key == pygame.K_LEFT:
                    print("\nLeft pressed")
                    print(object_list[0].position.x)
                    paddle.movePaddle('LEFT', SCREEN_SIZE[0])

        # TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
            # pass

        if len(object_list):
            if object_list[0].lives == 0:
                pygame.quit()
        for object in object_list:
            object.update()
            object.check_collision()

        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
