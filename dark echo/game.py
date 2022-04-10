import math
import pygame as pg

import vector

# 角色类


class Character:
    direct = [0.0, -1.0]  # 角色行走的方向向量
    v = 0  # 行走速度

    win = pg.Surface([0, 0])

    footprint = [[win.get_width() / 2, win.get_height() / 2], ]

    def __init__(self, win: pg.Surface) -> None:
        self.win = win

    def update(self, direct):
        if vector.get_mould(direct) == 0:
            return
        self.direct = vector.get_v(direct, 1)
        self.v = math.pi * math.sqrt(vector.get_mould(direct)) / math.e

    # 绘制脚印
    def draw_feet(self, win: pg.Surface):
        # 这个是临时的
        pg.draw.aaline(win, [255, 255, 255], [win.get_width() / 2, win.get_height() / 2],
                       vector.v_add([win.get_width() / 2, win.get_height() / 2], vector.get_v(self.direct, self.v)), 3)

    # 绘制角色
    # 脚印、声波等
    def draw(self, win: pg.Surface):
        self.draw_feet(win)
