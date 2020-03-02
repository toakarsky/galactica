import pygame


class Camera:
    _camera = None
    
    class _Camera:
        def __init__(self, GAME_WINDOW, BACKGROUND_COLOR=None, BACKGROUND_TILE_PATH=None, DEBUG=False):
            self.viewportSize = GAME_WINDOW.size
            self.renderOffset = (self.viewportSize[0] // 2, self.viewportSize[1] // 2)
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
                print('IMPLEMENT THIS')
                self.backgroundTileScreen = None
            
            self.screen = pygame.Surface(self.viewportSize)
            self.clearScreen()
        
        def clearScreen(self):
            self.screen.fill(self.backgroundColor)
            if self.backgroundTilePath != None:
                self.screen.blit(self.backgroundTileScreen, (0, 0))
        
        def updateWindow(self):
            self.windowScreen.blit(self.screen, (0, 0))
            pygame.display.update()
            self.clearScreen()
            
    
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