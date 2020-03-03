import pygame

from galactica import settings
from .events import Events


class Input:
    _input = None

    class _Input:
        def __init__(self, DEBUG):
            self.debug = DEBUG
            self.pressedButtons = []

            if self.debug:
                print('######################')
                print('Initializing new Input')

        def handle_events(self):
            for event in Events.GetEvents().getEventsByGroup("INPUT"):
                if event.type == pygame.KEYDOWN:
                    self.pressedButtons.append(event.key)
                    if self.debug:
                        print('***********')
                        print('FOUND EVENT')
                        print(f'pygame.KEYDOWN={event.key}')
                elif event.type == pygame.KEYUP:
                    self.pressedButtons.remove(event.key)
                    if self.debug:
                        print('***********')
                        print('FOUND EVENT')
                        print(f'pygame.KEYUP={event.key}')

        def update(self):
            self.handle_events()

        def isKeyPressed(self, key):
            return key in self.pressedButtons

    @staticmethod
    def GetInput(DEBUG=None):
        if Input._input == None:
            Input._input = Input._Input(
                DEBUG=DEBUG
            )
        return Input._input
