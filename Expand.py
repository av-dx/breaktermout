from Vector2 import Vector2
from Ball import Ball
from Paddle import Paddle
from Powerup import Powerup
from Globals import *


class Expand(Powerup):

    def __init__(self, position: Vector2) -> None:
        image = '<>'
        name = 'Expand'
        super().__init__(position, image, name)

    def start(self, paddle: Paddle, balls: list[Ball]) -> None:
        if paddle.size.x+10 < 50:
            paddle.size = Vector2(paddle.size.x+10, paddle.size.y)
        else:
            self.active = False
            return
        paddle.image = '#'*paddle.size.x
        paddle.makeSprite()
        self.timer = 100

    def execute(self, paddle: Paddle, balls: list[Ball]) -> None:
        pass

    def end(self, paddle: Paddle, balls: list[Ball]) -> None:
        paddle.size = Vector2(paddle.size.x-10, paddle.size.y)
        paddle.image = '#'*paddle.size.x
        paddle.makeSprite()
        for ball in balls:
            if ball.grabbed:
                ball.position.x = min(
                    ball.position.x, paddle.position.x + paddle.size.x - 2)
