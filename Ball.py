from Vector2 import *
from Globals import *
from Entity import Entity
from Paddle import Paddle
from Brick import Brick


class Ball(Entity):

    def __init__(self, position: Vector2 = nullVector2, dir: Vector2 = Vector2(-1, 1)) -> None:
        Entity.__init__(self, position, Vector2(1, 1), 'O', 'Ball')
        self.dir = dir
        self.speed = 1
        self.maxspeed = 1.5
        self.grabbed = False
        self.thrumode = False

    def move(self, collidables: list[Entity], paddle: Paddle) -> None:
        if self.grabbed:
            return
        oldPos = Vector2(self.position.x, self.position.y)
        Entity.move(self, self.dir*self.speed)
        borders = Vector2(BOARD_WIDTH, BOARD_HEIGHT)
        # if self.position.y >=

        if (paddle.position.x <= self.position.x < (paddle.position + paddle.size).x) \
                and (paddle.position.y <= self.position.y) and (oldPos.y < paddle.position.y):
            self.dir.x += 3 * (self.position.x -
                               paddle.position.x - paddle.size.x/2) / paddle.size.x
            self.position.y = paddle.position.y - 1
            self.position.x = oldPos.x
            self.dir.y = -self.dir.y
            self.speed += 0.01
            if (self.dir.x > self.maxspeed):
                self.dir.x = self.maxspeed
            if (self.dir.x < -self.maxspeed):
                self.dir.x = -self.maxspeed
            if paddle.grabmode:
                self.grabbed = True

        for ind, e in enumerate(collidables):
            if (e.position.y <= self.position.y < (e.position+e.size).y) \
                    and (e.position.x <= self.position.x < (e.position+e.size).x):
                e.hit(self)
                if self.thrumode and isinstance(e, Brick):
                    continue
                # print("I hit : ", e)
                self.position = oldPos
                if (oldPos.y >= (e.position + e.size).y):
                    # collided bottom
                    self.position.y = (e.position + e.size).y + 1
                    self.dir.y = -self.dir.y
                elif (oldPos.y <= e.position.y):
                    # collided top
                    self.position.y = e.position.y - 1
                    self.dir.y = -self.dir.y
                elif (oldPos.x >= (e.position + e.size).x):
                    # collided right
                    self.position.x = (e.position + e.size).x + 1
                    self.dir.x = -self.dir.x
                elif (oldPos.x <= e.position.x):
                    # collided left
                    self.position.x = e.position.x - 1
                    self.dir.x = -self.dir.x
                else:
                    # print("Idunno","I wanna move to:", self.position, "from:", oldPos, "but", e, "blocking me")
                    pass
                break
            else:
                pass
        # print("Idunno","I wanna move to:", self.position, "from:", oldPos, "with", self.dir, self.speed, "but", e, "blocking me")

        if (self.position.x > borders.x-2):
            self.position.x = borders.x-2
            self.dir.x = -self.dir.x
        if (self.position.y > borders.y-2):
            self.active = False
            # self.position.y = borders.y-2
            # self.dir.y = -self.dir.y
        if (self.position.x < 1):
            self.position.x = 1
            self.dir.x = -self.dir.x
        if (self.position.y < 1):
            self.position.y = 1
            self.dir.y = -self.dir.y

    def collide(self):
        pass
