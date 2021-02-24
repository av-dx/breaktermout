from Vector2 import Vector2
from Ball import Ball
from Paddle import Paddle
from Powerup import Powerup
from Globals import *


class Grab(Powerup):

    def __init__(self, position: Vector2) -> None:
        image = '╚╝'
        name = 'Grab'
        super().__init__(position, image, name)

    def start(self, paddle: Paddle, balls: list[Ball]) -> None:
        self.timer = 200

    def execute(self, paddle: Paddle, balls: list[Ball]) -> None:
        paddle.grabmode = True

    def end(self, paddle: Paddle, balls: list[Ball]) -> None:
        paddle.grabmode = False
