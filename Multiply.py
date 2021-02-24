from Vector2 import Vector2
from Powerup import Powerup
from Paddle import Paddle
from Ball import Ball
from Globals import *


class Multiply(Powerup):

    def __init__(self, position: Vector2) -> None:
        image = 'x2'
        name = 'Multiply'
        super().__init__(position, image, name)

    def start(self, paddle: Paddle, balls: list[Ball]) -> None:
        oldBalls = balls[:]
        for ball in oldBalls:
            balls.append(Ball(ball.position, Vector2(-ball.dir.x, ball.dir.y)))
        for ball in balls:
            ball.speed = ball.speed / 2
        self.timer = 20

    def execute(self, paddle: Paddle, balls: list[Ball]) -> None:
        return super().execute(paddle, balls)

    def end(self, paddle: Paddle, balls: list[Ball]) -> None:
        return super().end(paddle, balls)
