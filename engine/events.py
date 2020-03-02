import pygame


class Events:
    _events = None

    class _Events:
        def __init__(self, DEBUG=False):
            self.allEventsList = []
            self.debug = DEBUG

            if self.debug:
                print('#######################')
                print('Initializing new Events')

        def updateEventsList(self):
            self.allEventsList = pygame.event.get()

        def update(self):
            self.updateEventsList()

    def GetEvents(DEBUG=False):
        if Events._events == None:
            Events._events = Events._Events(
                DEBUG=DEBUG
            )
        return Events._events
