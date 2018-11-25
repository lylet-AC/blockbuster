import pygame as pg
from settings import *
import random


class Boundaries(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        # defines top boundary
        self.topimage = pg.Surface((WIDTH, 10))
        self.toprect = self.topimage.get_rect()
        self.toprect.x = 0
        self.toprect.y = 0
        # defines left boundary
        self.leftimage = pg.Surface((10, HEIGHT))
        self.leftrect = self.leftimage.get_rect()
        self.leftrect.x = 0
        self.leftrect.y = 0
        # defines right boundary
        self.rightimage = pg.Surface((10, HEIGHT))
        self.rightrect = self.rightimage.get_rect()
        self.rightrect.x = WIDTH - 10
        self.rightrect.y = 0
        # defines bottom boundary
        self.bottomimage = pg.Surface((WIDTH, 10))
        self.bottomrect = self.bottomimage.get_rect()
        self.bottomrect.x = 0
        self.bottomrect.y = HEIGHT - 10


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.lives = BALLS
        self.points = 0

    def move(self, dx=0):
        self.x += dx

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_text(self):
        score_str = "Score: " + str(self.points)
        life_str = "Lives: " + str(self.lives)

        self.score_box = self.game.bigfont.render(score_str, True, WHITE)
        self.game.screen.blit(self.score_box, (int(WIDTH / 2) - 100, 10))

        self.life_box = self.game.smallfont.render(life_str, True, WHITE)
        self.game.screen.blit(self.life_box, (10, HEIGHT - 25))


class Block(pg.sprite.Sprite):
    def __init__(self, game, x, y, color):
        self.groups = game.all_sprites, game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Ball(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.ball_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vector = self.random_vector()  # need to fix this

    def collide(self, dx=0, dy=0):
        # colliding with paddle
        if self.game.player.rect.colliderect(self.rect):
            self.reflect_x_vector()

        # colliding with walls
        if self.rect.colliderect(self.game.boundaries.toprect):
            self.reflect_x_vector()
        if self.rect.colliderect(self.game.boundaries.leftrect):
            self.reflect_y_vector()
        if self.rect.colliderect(self.game.boundaries.rightrect):
            self.reflect_y_vector()

        # colliding with death plane
        if self.rect.colliderect(self.game.boundaries.bottomrect):
            self.game.player.lives -= 1
            self.kill()
            self.game.new_ball()

        # colliding with blocks
        for block in self.game.blocks:
            if block.rect.colliderect(self.rect):
                self.reflect_x_vector()
                self.game.player.points += BLOCK_POINTS
                block.kill()

    def reflect_x_vector(self, dx=0):
        if self.vector[0] < 0:
            self.vector[0] = - self.vector[0]
        else:
            self.vector[0] = - self.vector[0]

    def reflect_y_vector(self):
        if self.vector[1] < 0:
            self.vector[1] = - self.vector[1]
        else:
            self.vector[1] = - self.vector[1]

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.collide(dx=BALL_SPEED, dy=BALL_SPEED)
        self.move()

    def move(self):
        self.y += self.vector[0]
        self.x += self.vector[1]

    def random_vector(self):
        horizontal_speed = random.randrange(-4, 4)  # x axis speed
        if horizontal_speed == 0:
            horizontal_speed = 5
        return [BALL_SPEED, horizontal_speed]
