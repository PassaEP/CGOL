from graphics import *
import math

a = 50 #the top corner coords.
b = 70 #the second bottom corner.
length = b - a
window_width = 800
window_height = 600
row_total = (window_width - (2 * a)) / length
col_total = (window_height - (2 * a)) / length
cell_total = row_total * col_total
#the cell class contains methods to init state, change state
#coordinates as well.

class Cell:

    stat = 0
    color = 'white'
    def change(self):
        if self.stat == 0:  # 0 is dead, 1 is alive. Start off dead, all of them.
            self.stat = 1
            self.color = 'blue2'
            self.sqr.setFill(self.color)
        else:
            self.stat = 0
            self.color = 'white'
            self.sqr.setFill(self.color)

    def loc(self, num):
        if num == 0:
            self.FC = Point(a,a)
            self.BC = Point(b,b)
            self.col = 0
            self.row_num = 0
            self.sqr = Rectangle(self.FC,self.BC)
        else:
            self.col = num % row_total #position in row.
            self.row_num = math.trunc(num / row_total)
            self.fA = a + (self.col * length) #the distance across
            self.fU = a + (self.row_num * length) #the distance up & down
            self.FC = Point(self.fA, self.fU) #the first corner
            self.BC = Point(self.fA + length, self.fU + length) #the second corner
            self.sqr = Rectangle(self.FC, self.BC)
            self.sqr.setFill(self.color)

def gridInit(case):
    screen = GraphWin("Conway's Game of Life", window_width, window_height, autoflush = False)
    for x in range(0, cell_total):
        j = Cell()
        j.loc(x)
        case.append(j)
        case[x].sqr.draw(screen)
        update()
    return screen
