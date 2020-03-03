import pygame

from galactica import settings


class Loop:
    _loop = None

    class _Loop:
        def __init__(self, GAME_WINDOW, CAMERA, INPUT, EVENTS, DEBUG=False):
            self.gameWindow = GAME_WINDOW
            self.camera = CAMERA
            self.events = EVENTS
            self.debug = DEBUG
            self.input = INPUT
            self.clock = pygame.time.Clock()
            self.stop = False

            if self.debug:
                print('#######################')
                print('Initializing new Loop')
                print(f'FRAMERATE: {settings.LOOP_FPS}')

        def run(self):
            delta = 0

            while self.stop == False:
                delta = self.clock.tick(settings.LOOP_FPS)

                self.events.update()
                self.camera.update(delta)
                self.gameWindow.update()

                # check important things
                if self.gameWindow.closed:
                    if self.debug:
                        print('@@@@@@@')
                        print('CLOSING')
                    return -1

                self.input.update()

    @staticmethod
    def GetLoop(GAME_WINDOW=None, CAMERA=None, INPUT=None, EVENTS=None, DEBUG=False):
        if Loop._loop == None:
            Loop._loop = Loop._Loop(
                GAME_WINDOW=GAME_WINDOW,
                CAMERA=CAMERA,
                EVENTS=EVENTS,
                INPUT=INPUT,
                DEBUG=DEBUG
            )
        return Loop._loop
