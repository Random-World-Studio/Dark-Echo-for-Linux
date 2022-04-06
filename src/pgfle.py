'''
pygame flow engine
'''
from pickle import STOP
import pygame as pg
import _thread
import random

fpsctl = pg.time.Clock()


class eveHandle:
    def __init__(self, event_t, handle) -> None:
        self.event_t = event_t
        self.handle = handle

    def getType(self):
        return self.event_t

    def getHandle(self):
        return self.handle


class flow:

    # states
    STOP = 0
    RUNNING = 1

    def __init__(self, fps: int, func, exitfunc=exit, *evelist: eveHandle) -> None:
        self.fps = fps
        self.func = func
        self.exitfunc = exitfunc
        self.evelist = evelist
        self.state = self.STOP

    def run(self):
        b = True
        while b and self.state == self.RUNNING:
            b = self.func()
            fpsctl.tick(self.fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.exitfunc(0)
                for which in self.evelist:
                    if event.type == which.getType():
                        which.getHandle()()

    def start(self):
        self.state = self.RUNNING
        _thread.start_new_thread(
            self.run, ("flow", int(random.random() * 100000), ))

    def stop(self):
        self.state = STOP
