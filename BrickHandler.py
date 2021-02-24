from Board import Board
from Vector2 import Vector2
from Brick import Brick
from Globals import *


class BrickHandler:

    def __init__(self, board: Board) -> None:
        self.gridSize = Vector2((board.size.x - 2) // 6,
                                (board.size.y - 11) // 2)
        self.grid = [[None for i in range(self.gridSize.x)]
                     for j in range(self.gridSize.y)]
        self.queuedScore = 0
        self.defaultLevel()

    def draw(self, board: Board) -> None:
        for row in self.grid:
            for brick in row:
                if brick is not None:
                    brick.draw(board)

    def getBricks(self) -> list:
        ret = []
        for row in self.grid:
            for brick in row:
                if brick is not None:
                    ret.append(brick)
        # ret = [brick for brick in (row for row in self.grid) if brick is not None]
        return ret

    def removeBrick(self, pos: Vector2) -> None:
        gridPos = Vector2((pos.x - 1) // 6, (pos.y - 1)//2)
        self.grid[gridPos.y][gridPos.x] = None
        self.queuedScore += 100

    def addBrick(self, gridPos: Vector2, type: int) -> None:
        renderPos = Vector2(gridPos.x * 6 + 1, gridPos.y * 2 + 1)
        newBrick = Brick(renderPos, type, self)
        self.grid[gridPos.y][gridPos.x] = newBrick

    def update(self) -> None:
        for i, row in enumerate(self.grid):
            for j, brick in enumerate(row):
                if brick is not None and not brick.active:
                    self.grid[i][j] = None
                    self.queuedScore += 100
        score = self.queuedScore
        self.queuedScore = 0
        return score

    def causeExplosion(self, pos: Vector2) -> None:
        gridPos = Vector2((pos.x - 1) // 6, (pos.y - 1)//2)
        neighbours = []
        neighbours.append(Vector2(max(gridPos.x - 1, 0), gridPos.y))
        neighbours.append(
            Vector2(min(gridPos.x + 1, self.gridSize.x-1), gridPos.y))
        neighbours.append(Vector2(gridPos.x, max(gridPos.y - 1, 0)))
        neighbours.append(Vector2(gridPos.x, min(
            gridPos.y + 1, self.gridSize.y - 1)))
        neighbours.append(
            Vector2(max(gridPos.x - 1, 0), max(gridPos.y - 1, 0)))
        neighbours.append(Vector2(max(gridPos.x - 1, 0),
                                  min(gridPos.y + 1, self.gridSize.y - 1)))
        neighbours.append(
            Vector2(min(gridPos.x + 1, self.gridSize.x-1), max(gridPos.y - 1, 0)))
        neighbours.append(Vector2(
            min(gridPos.x + 1, self.gridSize.x-1), min(gridPos.y + 1, self.gridSize.y - 1)))
        for n in neighbours:
            if self.grid[n.y][n.x] is not None:
                self.queuedScore += 100
                self.grid[n.y][n.x].hit(None, BRICK_STRENGTH_UNBREAKABLE)
                # self.update()

    def defaultLevel(self) -> None:
        for i in range(13):
            self.addBrick(Vector2(i+3, 1), BRICK_STRENGTH_BRITTLE)
        for i in range(13):
            self.addBrick(Vector2(i+3, 2), BRICK_STRENGTH_FULL)
        for i in range(13):
            self.addBrick(Vector2(i+3, 5), BRICK_STRENGTH_HALF)
        for i in range(13):
            self.addBrick(Vector2(i+3, 6), BRICK_STRENGTH_FULL)
        for i in range(3, 10):
            self.addBrick(Vector2(i+3, 2), BRICK_STRENGTH_EXPLOSIVE)
        for i in range(0, 3):
            self.addBrick(Vector2(i+3, 3), BRICK_STRENGTH_HALF)
        for i in range(3, 10):
            self.addBrick(Vector2(i+3, 3), BRICK_STRENGTH_UNBREAKABLE)
        for i in range(10, 13):
            self.addBrick(Vector2(i+3, 3), BRICK_STRENGTH_HALF)
        for i in range(13):
            self.addBrick(Vector2(i+3, 4), BRICK_STRENGTH_QUARTER)
        for i in range(1, 7):
            self.addBrick(Vector2(2, i), BRICK_STRENGTH_EXPLOSIVE)
        for i in range(1, 7):
            self.addBrick(Vector2(16, i), BRICK_STRENGTH_EXPLOSIVE)
        for i in range(1, 7):
            self.addBrick(Vector2(i+1, i), BRICK_STRENGTH_EXPLOSIVE)
        for i in range(1, 7):
            self.addBrick(Vector2(17-i, i), BRICK_STRENGTH_EXPLOSIVE)
