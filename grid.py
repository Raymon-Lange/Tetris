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

    def reset(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                self.grid[row][col] = 0

    def draw(self, screen):
        for row in range(self.numRows):
            for col in range(self.numCols):
                cellValue = self.grid[row][col]
                cellRect = pygame.Rect(col*self.cellSize + 11, row*self.cellSize + 11,
                self.cellSize -1, self.cellSize -1)
                pygame.draw.rect(screen, self.colors[cellValue], cellRect)

    def isInside(self, row, col):
        if row >=0 and row < self.numRows and col >= 0 and col < self.numCols:
            return True
        return False
    
    def isEmpty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        return False
        
    def isRowFull(self, row):
        for col in range(self.numCols):
            if self.grid[row][col] == 0:
                return False
        return True
        
    def clearRow(self, row):
         for col in range(self.numCols):
            self.grid[row][col] = 0

    def moveRowDown(self, row, numberRows):
        for col in range(self.numCols):
            self.grid[row + numberRows][col] = self.grid[row][col]
            self.grid[row][col]

    def clearFullRows(self):
        completedRows = 0
        for row in range(self.numRows-1, 0, -1):
            if self.isRowFull(row) == True:
                self.clearRow(row)
                completedRows += 1
            elif completedRows > 0:
                self.moveRowDown(row, completedRows)
        return completedRows
