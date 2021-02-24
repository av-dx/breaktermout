from Vector2 import *
from Entity import Entity
from Globals import BOARD_WIDTH


class Paddle(Entity):

    def __init__(self, position: Vector2, size: int) -> None:
        Entity.__init__(self, position-Vector2(size//2, 0),
                        Vector2(size, 1), '#'*size, 'Paddle')
        self.grabmode = True

    def move(self, step: Vector2, balls: list[Entity]) -> None:
        ballsRelativePosition = [None] * len(balls)
        for ind, ball in enumerate(balls):
            ballsRelativePosition[ind] = ball.position - self.position
        super().move(step)
        if self.position.x < 1:
            self.position.x = 1
        if self.position.x+self.size.x > BOARD_WIDTH-1:
            self.position.x = BOARD_WIDTH - self.size.x-1
        for ind, ball in enumerate(balls):
            if ball.grabbed:
                ball.position = self.position + ballsRelativePosition[ind]

    def release(self, balls: list[Entity]) -> None:
        for ball in balls:
            ball.grabbed = False
        self.grabmode = False
