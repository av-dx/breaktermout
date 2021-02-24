from random import randint
from Vector2 import Vector2
from InputHandler import InputHandler
from BrickHandler import BrickHandler
from Globals import *
from Ball import Ball
from Paddle import Paddle
from Board import Board
from Powerup import Powerup
from ThruBall import ThruBall
from SpeedUp import SpeedUp
from Multiply import Multiply
from Shrink import Shrink
from Expand import Expand
from Grab import Grab


class Game:

    def __init__(self) -> None:
        self.inputHandler = InputHandler()
        self.board = Board(size=Vector2(BOARD_WIDTH, BOARD_HEIGHT))
        self.brickHandler = BrickHandler(self.board)
        self.paddle = None
        self.balls = []
        self.powerUps = []
        self.activePowerUps = []
        self.score = 0
        self.lives = 5
        self.isRunning = True

    def start(self) -> None:
        self.score = 0
        self.balls = []
        self.powerUps = []
        self.paddle = Paddle(Vector2(BOARD_WIDTH//2, BOARD_HEIGHT-3), 10)
        self.balls.append(
            Ball(Vector2(BOARD_WIDTH//2+1, BOARD_HEIGHT - 4), Vector2(-1, 1)))
        self.brickHandler = BrickHandler(self.board)

    def over(self) -> None:
        print('{:<80}'.format("GAME OVER !"))
        self.inputHandler.exit()
        print("\x1b[?25h")
        self.isRunning = False

    def getState(self) -> tuple:
        return (self.score, self.lives, self.powerUps)

    def update(self) -> None:
        bs = self.brickHandler.getBricks()
        for power in self.powerUps:
            power.update(self.paddle, self.balls)
        for ball in self.balls:
            ball.move(bs, self.paddle)
        for bk in bs:
            if not bk.active:
                if randint(0, 5) == 1:
                    self.powerUps.append(spawnRandom((bk.position+bk.size/2)))
        self.balls = [bl for bl in self.balls if bl.active]
        self.score += self.brickHandler.update()
        self.powerUps = [power for power in self.powerUps if power.active]

        if (len(self.balls) <= 0):
            self.lives -= 1
            if self.lives < 1:
                self.over()
            else:
                self.start()
        if (len(bs) <= 0):
            self.over()

        if self.inputHandler.getKey('q'):
            self.over()
        elif self.inputHandler.getKey('a'):
            self.paddle.move(Vector2(-2, 0), self.balls)
        elif self.inputHandler.getKey('d'):
            self.paddle.move(Vector2(2, 0), self.balls)
        elif self.inputHandler.getKey(' '):
            self.paddle.release(self.balls)
        elif self.inputHandler.getKey('x'):
            self.over()

    def render(self) -> None:
        self.board.refresh()
        self.brickHandler.draw(self.board)
        waste = [power.draw(self.board) for power in self.powerUps]
        self.paddle.draw(self.board)
        waste = [ball.draw(self.board, ball.dir) for ball in self.balls]

        self.board.print()
        # print(self.brickHandler.gridSize, self.score, self.lives)

    def clearWithHUD(self) -> None:
        print("\033[F" * (BOARD_HEIGHT + 4))

    def clearWithoutHUD(self) -> None:
        print("\033[F" * (BOARD_HEIGHT + 2))


def spawnRandom(position: Vector2) -> Powerup:
    randType = randint(POWERUP_EXPAND, POWERUP_GRAB)
    if randType == POWERUP_GRAB:
        return Grab(position)
    elif randType == POWERUP_EXPAND:
        return Expand(position)
    elif randType == POWERUP_SHRINK:
        return Shrink(position)
    elif randType == POWERUP_MULTIPLY:
        return Multiply(position)
    elif randType == POWERUP_SPEEDUP:
        return SpeedUp(position)
    elif randType == POWERUP_THRUBALL:
        return ThruBall(position)
    else:
        return Powerup(position, POWERUP_GRAB)
