from brain import *
from graphics import *
import time
import random

# SOME GLOBAL VARIABLE NAMES:

# length
# window_width
# window_height
# row_total
# col_total
# cell_total

# They're pretty self-explanatory.


box = []

def start(grid, case):
    numAlive = random.randint(1,cell_total) #random number of cells
    for x in range(0, numAlive):
        cellMk = random.randint(0,cell_total - 1)
        case[cellMk].change()

    update()
    grid.flush
    return 0

board = gridInit(box) #making that grid.
start(board, box)
board.getMouse()
board.close()
