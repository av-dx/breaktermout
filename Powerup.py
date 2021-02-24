from Entity import *
from Ball import *
from Paddle import *
from Globals import *


class Powerup(Entity):

    def __init__(self, position: Vector2, image: str, name: str) -> None:
        image = image[:2]
        super().__init__(position=position, size=Vector2(2, 1), image=image, name=name)
        self.timer = 0
        self.ineffect = False

    def update(self, paddle: Paddle, balls: list[Ball]) -> None:
        self.move(Vector2(0, 0.2))
        if self.ineffect:
            self.timer -= 1
            self.execute(paddle, balls)
            if self.timer <= 0:
                self.end(paddle, balls)
                self.ineffect = False
                self.active = False
        if self.position.y >= BOARD_HEIGHT and not self.ineffect:
            self.active = False
        elif self.position >= paddle.position - Vector2(1, 1) and self.position <= paddle.position + paddle.size and not self.ineffect:
            self.start(paddle, balls)
            self.position.y = BOARD_HEIGHT
            self.ineffect = True
            self.image = '  '
            self.makeSprite()
        else:
            pass

    def start(self, paddle: Paddle, balls: list[Ball]) -> None:
        pass

    def execute(self, paddle: Paddle, balls: list[Ball]) -> None:
        pass

    def end(self, paddle: Paddle, balls: list[Ball]) -> None:
        pass
