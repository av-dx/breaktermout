from Vector2 import *
from Entity import *
from Globals import *


class Brick(Entity):

    def __init__(self, position: Vector2, type: int, handler=None) -> None:
        super().__init__(position=position, size=Vector2(6, 2), image='X', name='Brick')
        self.handler = handler
        self.strength = type
        self.makeImage()
        self.makeSprite()

    def hit(self, other: "Entity", hitStrength: int = 1) -> None:
        # print (self, "got hit! ", self.strength)
        if self.strength == BRICK_STRENGTH_EXPLOSIVE:
            if self.handler is not None:
                self.active = False
                if self.handler is not None:
                    self.handler.removeBrick(self.position)
                self.handler.causeExplosion(self.position)
        if self.strength != BRICK_STRENGTH_UNBREAKABLE or hitStrength >= BRICK_STRENGTH_UNBREAKABLE:
            self.strength -= hitStrength
        if other is not None and other.thrumode:
            self.strength = BRICK_STRENGTH_DESTROYED
        if self.strength <= BRICK_STRENGTH_DESTROYED:
            self.active = False
            # if self.handler is not None:
            #     self.handler.removeBrick(self.position)
        self.makeImage()
        self.makeSprite()

    def makeImage(self) -> None:
        if self.strength == BRICK_STRENGTH_BRITTLE:
            self.image = 'D'*(self.size.x*self.size.y)
        elif self.strength == BRICK_STRENGTH_QUARTER:
            self.image = 'C'*(self.size.x*self.size.y)
        elif self.strength == BRICK_STRENGTH_HALF:
            self.image = 'B'*(self.size.x*self.size.y)
        elif self.strength == BRICK_STRENGTH_FULL:
            self.image = 'A'*(self.size.x*self.size.y)
        elif self.strength == BRICK_STRENGTH_EXPLOSIVE:
            self.image = 'E'*(self.size.x*self.size.y)
        elif self.strength == BRICK_STRENGTH_UNBREAKABLE:
            self.image = 'Z'*(self.size.x*self.size.y)
        else:
            self.image = 'X'*(self.size.x*self.size.y)
