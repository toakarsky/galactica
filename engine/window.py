import pygame


class GameWindow:
    _gameWindow = None

    class _GameWindow:
        def __init__(self, WINDOW_SIZE=None, WINDOW_TITLE=None, WINDOW_ICON_PATH=None, DEBUG=False):
            self.size = WINDOW_SIZE
            self.title = WINDOW_TITLE
            self.iconPath = WINDOW_ICON_PATH
            self.debug = DEBUG
            
            if self.debug:
                print(f'Initializing new GameWindow')
                print(f'SIZE: {self.size}')
                print(f'TITLE: {self.title}')
                print(f'ICON: {self.iconPath}')
            
            if self.size == None:
                self.size = (640, 320)
            self.screen = pygame.display.set_mode(self.size)
            
            if self.title == None:
                self.title = "UNTITLED"
            pygame.display.set_caption(self.title)
            
            if self.iconPath != None:
                self.icon = pygame.image.load(self.iconPath)
                pygame.display.set_icon(self.icon)

    @staticmethod
    def GetGameWindow(WINDOW_SIZE=None, WINDOW_TITLE=None, WINDOW_ICON_PATH=None, DEBUG=False):
        if GameWindow._gameWindow == None:
            GameWindow._gameWindow = GameWindow._GameWindow(
                WINDOW_SIZE=WINDOW_SIZE,
                WINDOW_TITLE=WINDOW_TITLE,
                WINDOW_ICON_PATH=WINDOW_ICON_PATH,
                DEBUG=DEBUG
            )
        return GameWindow._gameWindow
