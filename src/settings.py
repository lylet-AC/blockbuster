import os

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# directories (mostly for images)
ROOT_FOLDER = os.path.dirname(__file__)  # root directory of the Game
SPRITE_FOLDER = os.path.join(ROOT_FOLDER, "sprites")  # sprite folder
# input image folder for mapgen
MAP_INPUT_FOLDER = os.path.join(ROOT_FOLDER, "input")
# test folder
TEST_FOLDER = os.path.join(ROOT_FOLDER, "tests")
LEVEL = "test_img.png"

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 45
TITLE = "Block Buster"
BGCOLOR = BLACK
BLOCK_POINTS = 10  # points per block

TILESIZE = 8
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
PADDLE_SPEED = 12
PADDLE_HEIGHT = 16
PADDLE_WIDTH = 128
BALLS = 3

# ball settings
BALL_SPEED = 12
BALL_SIZE = 16
