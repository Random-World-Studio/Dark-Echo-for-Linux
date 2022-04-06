'''
pygame flow engine
'''
import pygame as pg

class eveHandle:
    def __init__(self, event_t, handle : function) -> None:
        self.event_t = event_t
        self.handle = handle
    
    def getType(self):
        return self.event_t
    
    def getHandle(self) -> function:
        return self.handle

def run(func : function | bool, exitfunc : function, *evelist : eveHandle):
    while func():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exitfunc()
            for which in evelist:
                if event.type == which.getType():
                    which.getHandle()()
