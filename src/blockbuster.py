import pygame as pg
import sys
from settings import *
from sprites import *
from mapgen import generate_map


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(1, 1)
        self.load_data()

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.SysFont('symeteoiv50', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        self.player_img = pg.image.load(os.path.join(
            SPRITE_FOLDER, "paddle.png")).convert_alpha()
        self.player_img = pg.transform.scale(
            self.player_img, (PADDLE_WIDTH, PADDLE_HEIGHT))
        self.ball_img = pg.image.load(os.path.join(SPRITE_FOLDER, "ball.png"))
        self.ball_img = pg.transform.scale(
            self.ball_img, (BALL_SIZE, BALL_SIZE))
        self.block_img = pg.image.load(
            os.path.join(SPRITE_FOLDER, "block.png"))
        self.block_img = pg.transform.scale(
            self.block_img, (TILESIZE, TILESIZE))

        self.map_data = generate_map(LEVEL)
        self.bigfont = pg.font.SysFont('symeteoiv50', 40)
        self.smallfont = pg.font.SysFont('symeteoiv50', 30)

    def new_ball(self):
        self.ball = Ball(self, (WIDTH / 2) - (PADDLE_WIDTH / 2), HEIGHT - 70)
        self.player.x = ((WIDTH / 2) - (PADDLE_WIDTH - (BALL_SIZE / 2)))
        if(self.player.lives > 0):
            self.show_start_screen()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.blocks = pg.sprite.Group()
        self.player = Player(self, (WIDTH / 2) -
                             (PADDLE_WIDTH / 2), HEIGHT - 50)
        self.new_ball()
        for col, colors in enumerate(self.map_data):
            for row, color in enumerate(colors):
                if color == BLACK:
                    pass
                else:
                    Block(self, col, row + 2, color)

        self.boundaries = Boundaries(self)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        if len(self.blocks) == 0 or self.player.lives == 0:
            self.playing = False

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.player.draw_text()
        pg.display.flip()

    def events(self):
        # catch all events here
        pressed = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if pressed[pg.K_LEFT] and self.player.x > 12:
                    self.player.move(dx=-PADDLE_SPEED)
                if pressed[pg.K_RIGHT] and self.player.x < WIDTH - \
                        PADDLE_WIDTH - 12:
                    self.player.move(dx=PADDLE_SPEED)

    def show_start_screen(self):
        self.draw_text("Press a key to start", self.bigfont, 75,
                       WHITE, WIDTH / 2, HEIGHT * 3 / 4, align="center")
        pg.display.flip()
        self.wait_for_key()

    def show_gameover_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", self.bigfont, 100, RED,
                       WIDTH / 2, HEIGHT / 2, align="center")
        self.draw_text("Press a key to start", self.bigfont, 75,
                       WHITE, WIDTH / 2, HEIGHT * 3 / 4, align="center")
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_gameover_screen()
