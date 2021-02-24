from time import perf_counter

# UTF-8 symbols to shorten HUD
replaceDict = {
    'Expand': '➕',
    'Grab': '🧲',
    'Shrink': '➖',
    'Multiply': 'x2',
    'ThruBall': '🔴',
    'Speedup': '⏩',
    'Time': '⌛',
    'Lives': '💛',
    'Score': 'Score'
}


class HUD:

    def __init__(self) -> None:
        self.initTime = perf_counter()
        self.newTime = self.initTime
        self.timer = 0
        self.score = 0
        self.lives = 0
        self.activePowerups = {'GRAB': True, 'EXPAND': 54}

    def __str__(self) -> str:
        return str(self.score)+'HUD'

    def __repr__(self) -> str:
        return str(self.score)+'HUD'

    def update(self, score: int = -1, lives: int = -1, powerUps: list = []) -> None:
        self.newTime = perf_counter()
        self.timer = int(self.newTime - self.initTime)
        self.score = score
        self.lives = lives
        self.activePowerups.clear()
        for power in powerUps:
            if power.ineffect:
                if power.timer == -1:
                    self.activePowerups[power.name] = True
                else:
                    self.activePowerups[power.name] = power.timer

    def print(self) -> None:
        powerupstr = ''
        for p in self.activePowerups:
            powerupstr += replaceDict[p]
            if not isinstance(self.activePowerups[p], bool):
                powerupstr += '(' + str(self.activePowerups[p]) + '), '
            else:
                powerupstr += ', '
        # powerupstr = 'Expand(110), Grab(98), SpeedUp(14), '
        # Emoji HUD space is partitioned as follows (for the default 80 width)
        #  T:     L:    Score:        Powerups:
        # ________________________________________________________________________________
        #
        top = '⌛: {: 3} 💛: {: 2} Score: {: 6} Powerups: {:<40}'.format(
            self.timer, self.lives, self.score, powerupstr[:40])
        print(top)

    def instructions() -> None:
        print('Press X to quit safely.')
