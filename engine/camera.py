import pygame

from .tiled import TiledBackground
from .input import Input


class Camera:
    _camera = None

    class _Camera:
        def __init__(self, GAME_WINDOW, BACKGROUND_COLOR=None, BACKGROUND_TILE_PATH=None, DEBUG=False):
            self.viewportSize = GAME_WINDOW.size
            self.renderOffset = (self.viewportSize[0] //
                                 2, self.viewportSize[1] // 2)
            self.windowScreen = GAME_WINDOW.screen
            self.backgroundColor = BACKGROUND_COLOR
            self.backgroundTilePath = BACKGROUND_TILE_PATH
            self.debug = DEBUG

            if self.debug:
                print('#######################')
                print('Initializing new Camera')
                print(f'VIEWPORT_SIZE: {self.viewportSize}')
                print(f'RENDER_OFFSET: {self.renderOffset}')
                print(f'BACKGROUND_COLOR: {self.backgroundColor}')
                print(f'BACKGROUND_TILE_PATH: {self.backgroundTilePath}')

            if self.backgroundTilePath != None:
                self.backgroundTile = TiledBackground(
                    TILE_SIZE=self.viewportSize,
                    TILE_COUNT=3,
                    TILE_IMAGE_PATH=self.backgroundTilePath,
                    DEBUG=self.debug
                )

            self.screen = pygame.Surface(self.viewportSize)
            self.clearScreen()

        def clearScreen(self):
            self.screen.fill(self.backgroundColor)
            if self.backgroundTilePath != None:
                self.screen.blit(self.backgroundTile.renderScreen(), (0, 0))

        def updateWindow(self):
            self.windowScreen.blit(self.screen, (0, 0))
            pygame.display.update()
            self.clearScreen()

        def update(self, delta):
            if self.backgroundTilePath != None:
                if Input.GetInput().isKeyPressed(pygame.K_d):
                    self.backgroundTile.moveOffset((delta, 0))
                if Input.GetInput().isKeyPressed(pygame.K_a):
                    self.backgroundTile.moveOffset((-delta, 0))
                if Input.GetInput().isKeyPressed(pygame.K_s):
                    self.backgroundTile.moveOffset((0, delta))
                if Input.GetInput().isKeyPressed(pygame.K_w):
                    self.backgroundTile.moveOffset((0, -delta))

            self.updateWindow()

    @staticmethod
    def GetCamera(GAME_WINDOW=None, BACKGROUND_COLOR=None, BACKGROUND_TILE_PATH=None, DEBUG=False):
        if Camera._camera == None:
            Camera._camera = Camera._Camera(
                GAME_WINDOW=GAME_WINDOW,
                BACKGROUND_COLOR=BACKGROUND_COLOR,
                BACKGROUND_TILE_PATH=BACKGROUND_TILE_PATH,
                DEBUG=DEBUG
            )
        return Camera._camera
