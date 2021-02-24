from Vector2 import Vector2
from Ball import Ball
from Paddle import Paddle
from Powerup import Powerup
from Globals import *


class SpeedUp(Powerup):

    def __init__(self, position: Vector2) -> None:
        image = '>>'
        name = 'Speedup'
        super().__init__(position, image, name)

    def start(self, paddle: Paddle, balls: list[Ball]) -> None:
        self.timer = 100
        for ball in balls:
            ball.speed *= 1.25

    def execute(self, paddle: Paddle, balls: list[Ball]) -> None:
        pass

    def end(self, paddle: Paddle, balls: list[Ball]) -> None:
        for ball in balls:
            ball.speed /= 1.25
