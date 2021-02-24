import sys
import threading
from time import sleep
import tty
import termios


class InputHandler:

    def startPolling(self) -> None:
        timeout = 0
        while True:
            sleep(0.05)
            if timeout == 0:
                self.newChar = sys.stdin.read(1)
                while (sys.stdin.read(1) != ''):
                    sys.stdin.read(1)
            else:
                self.newChar = self.oldChar
                timeout -= 1
            if self.oldChar != self.newChar and self.newChar != '':
                timeout = 9
            try:
                self.keyDown[ord(self.oldChar)] = False
                self.oldChar = ''
            except:
                pass
            self.oldChar = self.newChar[:]
            if self.newChar != '':
                self.keyDown[ord(self.newChar)] = True

    def getKey(self, key: str) -> bool:
        return self.keyDown[ord(key)]

    def __init__(self) -> None:
        self.defSettings = termios.tcgetattr(sys.stdin)
        self.newSettings = termios.tcgetattr(sys.stdin)
        self.newSettings[tty.LFLAG] &= ~termios.ICANON
        self.newSettings[tty.LFLAG] &= ~termios.ECHO
        self.newSettings[tty.CC][termios.VMIN] = 0
        self.newSettings[tty.CC][termios.VTIME] = 0
        termios.tcsetattr(sys.stdin, termios.TCSANOW, self.newSettings)
        self.keyDown = [False] * 256
        self.oldChar, self.newChar = 'b', 'b'
        self.inputThread = threading.Thread(
            target=self.startPolling, daemon=True)
        self.inputThread.start()

    def exit(self) -> None:
        termios.tcsetattr(sys.stdin, termios.TCSANOW, self.defSettings)
