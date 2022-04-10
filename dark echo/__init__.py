import pygame as pg

import pgfle
import vector
import game
import sources

win = pg.Surface([0, 0])
_game = pgfle.Flow(0, None)

charac = game.Character(win)


def draw_cur(direct):  # 绘制鼠标特效,返回方向向量

    # 如果近似零向量
    if vector.get_mould(direct) < 10:
        pg.draw.line(win, [255, 0, 0], [_game.getMouse()[
                                            0] - 20, _game.getMouse()[1]],
                     [_game.getMouse()[0] + 20, _game.getMouse()[1]], 3)
        pg.draw.line(win, [255, 0, 0], [_game.getMouse()[0], _game.getMouse()[
            1] - 20], [_game.getMouse()[0], _game.getMouse()[1] + 20], 3)
        return

    # 计算箭尾坐标
    horiz = vector.get_horiz_v(direct, 22)
    negdir = vector.get_neg_v(direct)
    negdir = vector.get_v(negdir, 48)
    offset = vector.v_add(horiz, negdir)
    tail1 = vector.v_add(_game.getMouse(), offset)
    _horiz = vector.get_neg_v(horiz)
    offset = vector.v_add(_horiz, negdir)
    tail2 = vector.v_add(_game.getMouse(), offset)
    rt = vector.v_add(_game.getMouse(), vector.get_v(negdir, 18))
    pg.draw.polygon(win, [255, 255, 255], [
        _game.getMouse(), tail1, rt, tail2])
    pg.draw.aalines(win, [255, 255, 255], True, [
        _game.getMouse(), tail1, rt, tail2])


def flash() -> bool:  # 刷新函数
    # 清空屏幕
    pg.draw.rect(win, [0, 0, 0], [0, 0, win.get_width(), win.get_height()])

    direct = vector.v_sub(_game.getMouse(),
                          [win.get_width() / 2, win.get_height() / 2])

    # 绘制角色
    charac.update(direct)
    charac.draw(win)

    # 绘制鼠标
    draw_cur(direct)

    # 刷新屏幕
    pg.display.flip()
    return True


if __name__ == "__main__":
    pg.init()
    icon = pg.image.load('{}{}/icon.png'.format(sources.source_menu, sources.img_menu))
    pg.display.set_icon(icon)
    pg.display.set_caption('Dark Echo')
    pg.mouse.set_visible(False)
    win = pg.display.set_mode([1200, 680])
    # 初始化_game流
    _game = pgfle.Flow(60, flash)
    # 开启流
    _game.start()
