from Vector2 import Vector2
from Globals import *
from Ball import Ball
from Paddle import *
from Powerup import Powerup


class Shrink(Powerup):

    def __init__(self, position: Vector2) -> None:
        image = '><'
        name = 'Shrink'
        super().__init__(position, image, name)

    def start(self, paddle: Paddle, balls: list[Ball]) -> None:
        if paddle.size.x-5 > 4:
            paddle.size = Vector2(paddle.size.x-5, paddle.size.y)
        else:
            self.active = False
            return
        paddle.image = '#'*paddle.size.x
        paddle.makeSprite()
        self.timer = 100

    def execute(self, paddle: Paddle, balls: list[Ball]) -> None:
        pass

    def end(self, paddle: Paddle, balls: list[Ball]) -> None:
        paddle.size = Vector2(paddle.size.x+5, paddle.size.y)
        paddle.image = '#'*paddle.size.x
        paddle.makeSprite()
