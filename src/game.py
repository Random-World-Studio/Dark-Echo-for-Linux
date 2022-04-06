from typing import List
import pygame as pg

class wave:
    GROUND = 0
    TREASURE = 1
    DEADLY = 2
    WATER = 3
    
    MAXWIDTH = 10
    
    def __init__(self, position : List[int, int], maxBri, direction : List[int, int], decrement) -> None:
        self.position = position
        self.maxBri = maxBri
        self.bright = maxBri
        self.direction = direction
        self.decrement = decrement
        self.width = 10
        self.widDecr = self.MAXWIDTH * self.maxBri / self.decrement
    
    def refresh(self):
        self.bright -= self.decrement
        self.width -= self.widDecr
