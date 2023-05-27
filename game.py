from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()
        self.gameOver = False

    def getRandomBlock(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.currentBlock.draw(screen)

    def blockInside(self):
        tiles = self.currentBlock.getCellPos()
        for tile in tiles:
            if self.grid.isInside(tile.row, tile.col) == False:
                return False
        return True

    def moveLeft(self):
        self.currentBlock.move(0,-1)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0,1)
    
    def moveRight(self):
        self.currentBlock.move(0,1)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0,-1)

    def moveDown(self):
        self.currentBlock.move(1,0)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(-1,-0)
            self.lockBlock()


    def rotateBlock(self):
        self.currentBlock.rotate()
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.undoRotate()

    def lockBlock(self):
        tiles = self.currentBlock.getCellPos()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.currentBlock.id
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()
        self.grid.clearFullRows()

        if self.blockFits() == False:
            self.gameOver = True

    def blockFits(self):
        tiles = self.currentBlock.getCellPos()
        for tile in tiles:
            if self.grid.isEmpty(tile.row, tile.col) == False:
                return False
        return True
