from brain import *
from graphics import *
import math
import time
import random

box = []

def start(board):
    numAlive = random.randint(1,cell_total) #random number of cells
    for x in range(0, numAlive):
        cellMk = random.randint(0,cell_total - 1)
        box[cellMk].change()
        board.flush()
        update()
    return 0

board = gridInit(box) #making that grid.
board.getMouse()
start(board)
board.getMouse()
board.close()
