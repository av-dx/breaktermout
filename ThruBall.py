from Vector2 import Vector2
from Ball import Ball
from Paddle import Paddle
from Powerup import Powerup
from Globals import *


class ThruBall(Powerup):

    def __init__(self, position: Vector2) -> None:
        image = '->'
        name = 'ThruBall'
        super().__init__(position, image, name)

    def start(self, paddle: Paddle, balls: list[Ball]) -> None:
        self.timer = 200

    def execute(self, paddle: Paddle, balls: list[Ball]) -> None:
        for ball in balls:
            ball.thrumode = True
            ball.image = 'R'
            ball.makeSprite()

    def end(self, paddle: Paddle, balls: list[Ball]) -> None:
        for ball in balls:
            ball.thrumode = False
            ball.image = 'O'
            ball.makeSprite()
