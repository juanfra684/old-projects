class Board(object):
	UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4

class keypress(object):
	
	UP, DOWN, LEFT, RIGHT = 65, 66, 68, 67
	

class Game(object):
	dirs = {
        keypress.UP:      Board.UP,
        keypress.DOWN:    Board.DOWN,
        keypress.LEFT:    Board.LEFT,
        keypress.RIGHT:   Board.RIGHT,
    }

print(Game.dirs.get(65))
print(Game.dirs.get(66))
print(Game.dirs.get(67))
print(Game.dirs.get(68))
