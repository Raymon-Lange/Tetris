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
        self.linesClear = 0
        self.score = 0
        self.level = 1

    def getRandomBlock(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()
        self.linesClear = 0
        self.score = 0
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.currentBlock.draw(screen, 11,11)

        if self.nextBlock.id == 3:
            self.nextBlock.draw(screen, 255, 90)
        elif self.nextBlock.id == 4:
            self.nextBlock.draw(screen, 255, 90)
        else:
            self.nextBlock.draw(screen, 270, 90)


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

        lines = self.grid.clearFullRows()
        self.linesClear += lines
        self.calcScore(lines)
        self.level = int((self.linesClear / 10) +1)

        if self.blockFits() == False:
            self.gameOver = True

    def blockFits(self):
        tiles = self.currentBlock.getCellPos()
        for tile in tiles:
            if self.grid.isEmpty(tile.row, tile.col) == False:
                return False
        return True
    
    def calcScore(self, lineClear):
        if lineClear == 1:
            self.score += 40 * self.level
        elif lineClear == 2:
            self.score += 100 * self.level
        elif lineClear == 3:
            self.score += 300 * self.level
        elif lineClear == 4:
            self.score += 1200 * self.level


