from os import system
import re
from Vector2 import *
from Globals import *


def color(m):
    matched = m.group()

    if matched[0] == 'A':
        COL = COLOR_BG_RED
    elif matched[0] == 'B':
        COL = COLOR_BG_YELLOW
    elif matched[0] == 'C':
        COL = COLOR_BG_GREEN
    elif matched[0] == 'D':
        COL = COLOR_BG_BLUE
    elif matched[0] == 'E':
        COL = COLOR_BG_MAGENTA
    elif matched[0] == '#':
        COL = COLOR_BG_WHITE
    elif matched[0] == 'Z':
        COL = COLOR_BG_CYAN
    elif matched[0] == 'R':
        return COLOR_FG_RED + 'O' + COLOR_END
    elif matched in ['<>', '->', 'x2', '╚╝']:
        return COLOR_MIX(COLOR_BG_GREEN, COLOR_FG_BLACK) + matched + COLOR_END
    elif matched in ['><', '>>']:
        return COLOR_MIX(COLOR_BG_RED, COLOR_FG_WHITE) + matched + COLOR_END
    else:
        COL = COLOR_BG_BLUE
    length = len(matched)
    return COL+(' '*length)+COLOR_END


class Board:
    boardStrlen = 0

    def __init__(self, size: Vector2) -> None:
        self.size = size
        self.background = ['╔'+'═'*(size.x-2)+'╗'] + \
            ['║'+' '*(size.x-2)+'║'] * (size.y-1)
        self.board = []
        system('clear')
        print("\x1b[?25l")

    def print(self) -> None:
        b = ''
        for l in self.board:
            l = re.sub(r'(A+|B+|C+|D+|E+|Z+|R|#+)', color, l)
            l = re.sub(r'(<>|><|->|>>|x2|╚╝)', color, l)
            # l = re.sub(r'([|-])', r'\033[0;42m\1\033[0m', l)
            b = b + l + '\n'
        print(b[:-1])
        Board.boardStrlen = len(b)

    def refresh(self) -> None:
        self.board = self.background[:]
