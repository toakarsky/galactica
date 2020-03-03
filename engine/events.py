import json

import pygame

from galactica import settings


class Events:
    _events = None

    class _Events:
        def __init__(self, DEBUG=False):
            self.allEventsList = []
            self.groupByEventTypeMap = {}
            self.eventsByGroupMap = {}
            for eventGroup in settings.EVENTS_MAPPING.keys():
                self.eventsByGroupMap[eventGroup] = []
                for eventType in settings.EVENTS_MAPPING[eventGroup]:
                    self.groupByEventTypeMap[eventType] = eventGroup

            self.debug = DEBUG

            if self.debug:
                print('#######################')
                print('Initializing new Events')
                print(
                    f'MAPPING: {json.dumps(settings.EVENTS_MAPPING, indent=4)}')

        def updateEventsList(self):
            for eventGroup in self.eventsByGroupMap.keys():
                self.eventsByGroupMap[eventGroup] = []
            self.allEventsList = pygame.event.get()

        def getEventsByGroup(self, eventsGroup):
            if eventsGroup in self.eventsByGroupMap:
                return self.eventsByGroupMap[eventsGroup]
            return []

        def update(self):
            self.updateEventsList()

            for event in self.allEventsList:
                if event.type == pygame.QUIT and 'QUIT' in self.groupByEventTypeMap:
                    self.eventsByGroupMap[self.groupByEventTypeMap['QUIT']].append(
                        event)
                elif event.type == pygame.KEYUP and 'KEYUP' in self.groupByEventTypeMap:
                    self.eventsByGroupMap[self.groupByEventTypeMap['KEYUP']].append(
                        event)
                elif event.type == pygame.KEYDOWN and 'KEYDOWN' in self.groupByEventTypeMap:
                    self.eventsByGroupMap[self.groupByEventTypeMap['KEYDOWN']].append(
                        event)

    def GetEvents(DEBUG=False):
        if Events._events == None:
            Events._events = Events._Events(
                DEBUG=DEBUG
            )
        return Events._events
