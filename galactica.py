import pygame

import galactica.settings as settings
from engine.events import Events
from engine.window import GameWindow
from engine.camera import Camera
from engine.input import Input
from engine.loop import Loop


if __name__ == "__main__":
    pygame.init()

    window = GameWindow.GetGameWindow(
        WINDOW_SIZE=settings.WINDOW_SIZE,
        WINDOW_TITLE=settings.WINDOW_TITLE,
        WINDOW_ICON_PATH=settings.WINDOW_ICON_PATH,
        DEBUG=settings.WINDOW_DEBUG,
    )

    camera = Camera.GetCamera(
        GAME_WINDOW=window,
        BACKGROUND_COLOR=settings.CAMERA_BACKGROUND_COLOR,
        BACKGROUND_TILE_PATH=settings.CAMERA_BACKGROUND_TILE_PATH,
        DEBUG=settings.CAMERA_DEBUG
    )

    events = Events.GetEvents(
        DEBUG=settings.EVENTS_DEBUG
    )

    input = Input.GetInput(
        DEBUG=settings.INPUT_DEBUG
    )

    loop = Loop.GetLoop(
        GAME_WINDOW=window,
        CAMERA=camera,
        EVENTS=events,
        INPUT=input,
        DEBUG=settings.LOOP_DEBUG
    )

    loop.run()
