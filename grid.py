import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.numRows = 20
        self.numCols = 10
        self.cellSize = 30
        #STEP: Load a board with 0, zero stands for empty
        self.grid = [[0 for j in range(self.numCols)] for i in range(self.numRows)]
        self.colors = Colors.get_cell_colors()

    def printGrid(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                print(self.grid[row][col], end = " ")
            print()

    def draw(self, screen):
        for row in range(self.numRows):
            for col in range(self.numCols):
                cellValue = self.grid[row][col]
                cellRect = pygame.Rect(col*self.cellSize + 1, row*self.cellSize + 1,
                self.cellSize -1, self.cellSize -1)
                pygame.draw.rect(screen, self.colors[cellValue], cellRect)



