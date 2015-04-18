import sys
from game import Game


def start_game():
    game = Game()
    return game.loop()

start_game()
