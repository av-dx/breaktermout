from time import sleep
from HUD import *
from Game import Game

hud = HUD()
game = Game()

game.start()

while game.isRunning:
    gameState = game.getState()
    game.clearWithHUD()
    game.update()
    hud.update(gameState[0], gameState[1], gameState[2])
    hud.print()
    game.render()
    # print(game.balls[0].position, game.balls[0].dir, game.balls[0].speed, "         ")
    sleep(0.06)
