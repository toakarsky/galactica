import pygame

import galactica.settings as settings
from engine.window import GameWindow


if __name__ == "__main__":
    pygame.init()

    window = GameWindow.GetGameWindow(
        WINDOW_SIZE=settings.WINDOW_SIZE,
        WINDOW_TITLE=settings.WINDOW_TITLE,
        WINDOW_ICON_PATH=settings.WINDOW_ICON_PATH,
        DEBUG=settings.WINDOW_DEBUG,
    )
    
    n = input()
