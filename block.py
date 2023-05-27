import pygame
from colors import Colors
from position import Position

class Block:
    def __init__(self,id):
        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rotationState = 0
        self.colors = Colors.get_cell_colors()

        self.xPos = 0
        self.yPos = 0

    def move(self, row, col):
        self.xPos += row
        self.yPos += col

    def getCellPos(self):
        tiles = self.cells[self.rotationState]
        movedTiles = []
        for pos in tiles:
            pos = Position(pos.row + self.xPos, pos.col + self.yPos)
            movedTiles.append(pos)
        return movedTiles


    def draw(self, screen):
        tiles = self.getCellPos()
        for tile in tiles:
            tileRect= pygame.Rect(tile.col * self.cellSize+1, tile.row * self.cellSize +1, self.cellSize -1, self.cellSize -1)
            pygame.draw.rect(screen, self.colors[self.id], tileRect)
