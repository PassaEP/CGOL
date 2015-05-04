from graphics import *
import math

a = 10 #the top corner coords. 
b = 30 #the second bottom corner. 
length = b - a
window_width = 800
window_height = 600
cell_total = ((window_width - 20) * (window_height - 20)) / (length * length)
#the cell class contains methods to init state, change state
#coordinates as well. 

class Cell:

    stat = 0
    def change(self):
        if self.stat == 0: 
            self.stat = 1
        else: 
            self.stat = 0

    def loc(self, num): 
        if num == 0: 
            self.FC = Point(a,a)
            self.BC = Point(b,b)
            self.col = 0
            self.row_num = 0 
            self.sqr = Rectangle(self.FC,self.BC)
        else: 
            self.col = num % 39 #position in row. 
            self.row_num = math.trunc(num / 39)
            self.fA = a + (self.col * 20) #the distance across 
            self.fU = a + (self.row_num * 20) #the distance up & down
            self.FC = Point(self.fA, self.fU) #the first corner
            self.BC = Point(self.fA + 20, self.fU + 20) #the second corner 
            self.sqr = Rectangle(self.FC, self.BC) 



box = []


def gridInit(): 
    screen = GraphWin("Conway's Game of Life", window_width, window_height)
    for x in range(0, cell_total): 
        j = Cell()
        j.loc(x)
        box.append(j)
        box[x].sqr.draw(screen)
    screen.getMouse() # pause for click in window
    screen.close()

gridInit()
