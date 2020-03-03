import math

import pygame


class Tiled:
    def __init__(self, TILE_SIZE, TILE_COUNT, DEBUG=False):
        self.tileSize = TILE_SIZE
        self.tileCount = TILE_COUNT

        self.debug = DEBUG
        if self.debug:
            print('######################')
            print('Initializing new Tiled')
            print(f'TILE_SIZE: {self.tileSize}')
            print(f'TILE_COUNT: {self.tileCount}')

        self.screen = pygame.Surface(self.tileSize)
        self.tiles = [
            [
                pygame.Surface(self.tileSize) for _ in range(self.tileCount)
            ] for _ in range(self.tileCount)
        ]

        self.offset = (0, 0)

    def moveOffset(self, change):
        self.offset = (self.offset[0] + change[0], self.offset[1] + change[1])
        if self.offset[0] > (self.tileCount // 2) * self.tileSize[0]:
            if self.debug:
                print('-----------------')
                print('MOVING TILE TO -X')
            self.offset = (-(self.tileCount // 2) *
                           self.tileSize[0], self.offset[1])
        elif self.offset[0] < -(self.tileCount // 2) * self.tileSize[0]:
            if self.debug:
                print('-----------------')
                print('MOVING TILE TO X')
            self.offset = ((self.tileCount // 2) *
                           self.tileSize[0], self.offset[1])
        if self.offset[1] > (self.tileCount // 2) * self.tileSize[1]:
            if self.debug:
                print('-----------------')
                print('MOVING TILE TO -Y')
            self.offset = (
                self.offset[0], -(self.tileCount // 2) * self.tileSize[1])
        elif self.offset[1] < -(self.tileCount // 2) * self.tileSize[1]:
            if self.debug:
                print('-----------------')
                print('MOVING TILE TO Y')
            self.offset = (
                self.offset[0], (self.tileCount // 2) * self.tileSize[1])


class TiledBackground(Tiled):
    def __init__(self, TILE_SIZE, TILE_COUNT, TILE_IMAGE_PATH, DEBUG=False):
        super().__init__(TILE_SIZE, TILE_COUNT, DEBUG)
        TILE_SCALE = 4
        self.tileImagePath = TILE_IMAGE_PATH
        if self.debug:
            print(f'TILE_IMAGE_PATH: {self.tileImagePath}')

        self.tileImage = pygame.image.load(self.tileImagePath)
        self.tileImage = pygame.transform.scale(
            self.tileImage, (TILE_SCALE * self.tileImage.get_width(), TILE_SCALE * self.tileImage.get_height()))
        tileImageCount = (math.ceil(self.tileSize[0] / self.tileImage.get_width(
        )), math.ceil(self.tileSize[1] / self.tileImage.get_height()))
        renderMargin = (-(self.tileSize[0] % self.tileImage.get_width() // 2), -(
            self.tileSize[1] % self.tileImage.get_height() // 2))
        for tileRow in self.tiles:
            for tile in tileRow:
                for y in range(tileImageCount[1]):
                    for x in range(tileImageCount[0]):
                        tile.blit(self.tileImage, (x * self.tileImage.get_width(
                        ) + renderMargin[0], (y * self.tileImage.get_height() + renderMargin[1])))

    def clear(self):
        self.screen.fill((0, 0, 0))

    def renderTileOnScreen(self, tileRow, tileColumn):
        baseRenderPosition = (-((self.tileCount // 2) *
                                self.tileSize[0]), -((self.tileCount // 2) * self.tileSize[1]))
        currentTileRenderPosition = (
            baseRenderPosition[0] + tileColumn * self.tileSize[0], baseRenderPosition[1] + tileRow * self.tileSize[1])
        self.screen.blit(self.tiles[tileRow][tileColumn], (currentTileRenderPosition[0] -
                                                           self.offset[0], currentTileRenderPosition[1] - self.offset[1]))

    def composeTiles(self):
        for tileRow in range(self.tileCount):
            for tileColumn in range(self.tileCount):
                self.renderTileOnScreen(tileRow, tileColumn)

    def renderScreen(self):
        self.clear()
        self.composeTiles()
        return self.screen
