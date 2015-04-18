#Librerias de proposito general:
import os
import os.path
import math
import sys
#Libreria para formato de texto en consola:
from colorama import init, Fore, Style
init(autoreset=True)
#Librerias del juego:
import keypress
from board import Board

class Game(object):
    #Asignacion de teclas de direccion
    __dirs = {
        keypress.UP:      Board.UP,
        keypress.DOWN:    Board.DOWN,
        keypress.LEFT:    Board.LEFT,
        keypress.RIGHT:   Board.RIGHT,
    }
    #Diccionario con los colores:
    COLORS = {
        2:    Fore.GREEN,
        4:    Fore.BLUE + Style.BRIGHT,
        8:    Fore.CYAN,
        16:   Fore.RED,
        32:   Fore.MAGENTA,
        64:   Fore.CYAN,
        128:  Fore.BLUE + Style.BRIGHT,
        256:  Fore.MAGENTA,
        512:  Fore.GREEN,
        1024: Fore.RED,
        2048: Fore.YELLOW,
        4096: Fore.RED,
        8192: Fore.CYAN,
    }

    def __init__(self, colors=COLORS, clear_screen=True, azmode=False):
        #Inicializa el juego
        self.board = Board()
        self.score = 0
        self.clear_screen = clear_screen
        self.__colors = colors
        self.__azmode = azmode

    def updateScore(self, pts):
        self.score += pts


    def readMove(self):
        #Lee un movimiento y lo pasa al tablero
        k = keypress.getKey()
        return Game.__dirs.get(k)

    def clearScreen(self):
        #Limpia la pantalla:
        if self.clear_screen:
            os.system('clear')
        else:
            print('\n')

    def loop(self):
        #Inicializa el juego:
        margins = {'left': 3, 'top': 3, 'bottom': 3}
        try:
            while True:
                self.clearScreen()
                print(self.__str__(margins=margins))
                if self.board.win() or not self.board.canMove():
                    break
                direction = self.readMove()
                self.updateScore(self.board.move(direction))

        except KeyboardInterrupt:
            return

        print('You win!' if self.board.win() else 'Game Over')
        return self.score

    def getCellStr(self, x, y):  # TODO: refactor regarding issue #11
        """
        return a string representation of the cell located at x,y.
        """
        c = self.board.getCell(x, y)

        if c == 0:
            return '.' if self.__azmode else '  .'

        elif self.__azmode:
            az = {}
            for i in range(1, int(math.log(self.board.goal(), 2))):
                az[2 ** i] = chr(i + 96)

            if c not in az:
                return '?'
            s = az[c]
        elif c == 1024:
            s = ' 1k'
        elif c == 2048:
            s = ' 2k'
        else:
            s = '%3d' % c

        return self.__colors.get(c, Fore.RESET) + s + Style.RESET_ALL

    def boardToString(self, margins={}):
        """
        return a string representation of the current board.
        """
        b = self.board
        rg = range(b.size())
        left = ' '*margins.get('left', 0)
        s = '\n'.join(
            [left + ' '.join([self.getCellStr(x, y) for x in rg]) for y in rg])
        return s

    def __str__(self, margins={}):
        b = self.boardToString(margins=margins)
        top = '\n'*margins.get('top', 0)
        bottom = '\n'*margins.get('bottom', 0)
        scores = ' \tScore: %5d\n' % (self.score)
        return top + b.replace('\n', scores, 1) + bottom
