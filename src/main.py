import pygame as pg
import math

import pgfle
import game
import vector
import math


win = pg.Surface([0, 0])
_game = pgfle.flow(0, None)

charac = game.character()

mousearr_size = 36


def draw_cur():  # 绘制鼠标特效
    direct = vector.v_sub(_game.get_mouse(),
                          [win.get_width() / 2, win.get_height() / 2])
    
    # 如果近似零向量
    if vector.get_mould(direct) < 5:
        return

    # 计算箭尾坐标
    horiz = vector.get_horiz_v(direct, 16)
    negdir = vector.get_neg_v(direct)
    negdir = vector.get_v(negdir, 18)
    offset = vector.v_add(horiz, negdir)
    tail1 = vector.v_add(_game.get_mouse(), offset)
    _horiz = vector.get_neg_v(horiz)
    offset = vector.v_add(_horiz, negdir)
    tail2 = vector.v_add(_game.get_mouse(), offset)
    rt = vector.v_sub(_game.get_mouse(), vector.get_v(negdir, 12))
    pg.draw.polygon(win, [255, 255, 255], [
                    _game.get_mouse(), tail1, rt, tail2])


def flash() -> bool:  # 刷新函数
    # 清空屏幕
    pg.draw.rect(win, [0, 0, 0], [0, 0, win.get_width(), win.get_height()])

    # 绘制角色
    charac.draw(win)

    # 绘制鼠标
    draw_cur()

    # 刷新屏幕
    pg.display.flip()
    return True


# 初始化_game流
_game = pgfle.flow(60, flash)

if __name__ == "__main__":
    pg.init()
    icon = pg.image.load('./source/img/icon.png')
    pg.display.set_icon(icon)
    pg.display.set_caption('Dark Echo')
    pg.mouse.set_visible(False)
    win = pg.display.set_mode([1200, 680])

    # 开启流
    _game.start()
