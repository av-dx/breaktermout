import math
from Vector2 import *
from Board import *


class Entity:

    EntityList = []

    def __init__(self, position: Vector2 = nullVector2, size: Vector2 = Vector2(1, 1), image: str = '.', name: str = 'None') -> None:
        self.position = Vector2.__floor__(position)
        self.size = Vector2.__floor__(size)
        self.image = image
        self.sprite = []
        self.name = name
        self.active = True
        self.makeSprite()
        Entity.EntityList.append(self)

    def makeSprite(self) -> None:
        width = self.size.x
        height = self.size.y
        sprite = []
        length = len(self.image)
        for h in range(height):
            line = ''
            for w in range(width):
                if (0 <= h*width + w < length):
                    line += self.image[h*width + w]
                else:
                    line += 'X'
            sprite.append(line)
        self.sprite = sprite

    def __str__(self) -> str:
        return (f'Entity: "{self.name}" at (x, y) = {self.position} of size (w, h) = {self.size}\n'
                f'{self.image}')

    def draw(self, board: Board, dir: Vector2 = None) -> list:
        pos = Vector2(0, 0)
        pos.y = math.floor(self.position.y)
        pos.x = math.ceil(self.position.x)
        size = math.ceil(self.size)
        border = math.ceil(board.size)
        scanner = pos.y
        for h in range(size.y):
            if (0 <= scanner < board.size.y):
                line = self.sprite[scanner-pos.y]
                if (pos.x < border.x and (pos+size).x > 0):
                    # Draw
                    # x1 : index of str in line to start
                    x1 = max(0, -pos.x)
                    # x2 : index of str in line to end before
                    x2 = min(size.x, (border-pos).x)
                    # dx1 : index of str in board[y] to start
                    dx1 = max(0, pos.x)
                    # dx2 : index of str in board[y] to end before
                    dx2 = min(border.x, (pos+size).x)
                    board.board[scanner] = board.board[scanner][:dx1] + \
                        line[x1:x2] + board.board[scanner][dx2:]
                else:
                    # dont draw
                    pass
                scanner += 1

    def move(self, step: Vector2) -> None:
        self.position += Vector2(step.x, step.y)

    def hit(self, other: "Entity") -> None:
        pass

    def cleanup() -> None:
        oldList = Entity.EntityList[:]
        Entity.EntityList = [e for e in oldList if e.active]
