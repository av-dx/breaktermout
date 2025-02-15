BOARD_WIDTH = 120
BOARD_HEIGHT = 40


def COLOR_MIX(bgcol, fgcol):
    bg = bgcol[4:6]
    fg = fgcol[4:6]
    return '\033['+fg+';'+bg+'m'


COLOR_BG_BLACK = '\033[0;40m'
COLOR_BG_RED = '\033[0;41m'
COLOR_BG_GREEN = '\033[0;42m'
COLOR_BG_YELLOW = '\033[0;43m'
COLOR_BG_BLUE = '\033[0;44m'
COLOR_BG_MAGENTA = '\033[0;45m'
COLOR_BG_CYAN = '\033[0;46m'
COLOR_BG_WHITE = '\033[0;107m'

COLOR_FG_BLACK = '\033[0;30m'
COLOR_FG_RED = '\033[0;31m'
COLOR_FG_GREEN = '\033[0;32m'
COLOR_FG_YELLOW = '\033[0;33m'
COLOR_FG_BLUE = '\033[0;34m'
COLOR_FG_MAGENTA = '\033[0;35m'
COLOR_FG_CYAN = '\033[0;36m'
COLOR_FG_WHITE = '\033[0;97m'

COLOR_NONE = '\033[0m'
COLOR_END = '\033[0m'


BRICK_STRENGTH_EXPLOSIVE = 6
BRICK_STRENGTH_UNBREAKABLE = 5
BRICK_STRENGTH_FULL = 4
BRICK_STRENGTH_HALF = 3
BRICK_STRENGTH_QUARTER = 2
BRICK_STRENGTH_BRITTLE = 1
BRICK_STRENGTH_DESTROYED = 0

POWERUP_EXPAND = 0
POWERUP_SHRINK = 1
POWERUP_MULTIPLY = 2
POWERUP_SPEEDUP = 3
POWERUP_THRUBALL = 4
POWERUP_GRAB = 5
POWERUP_TEST = 6


HUD_ASCII_MODE = 0
HUD_UTF8_MODE = 1
