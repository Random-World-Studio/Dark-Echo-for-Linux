from typing import List
import pygame as pg

import source as src

# 角色类
class character:
    direct = [0.0, -1.0]# 角色行走的方向向量
    feetl_img = pg.transform.scale(pg.image.load("{}{}/feet.png".format(src.source_menu, src.img_menu)), [8, 20])# 左脚脚印的图像
    feetr_img = pg.transform.flip(feetl_img, True, False)# 翻转之后就是右脚
    v = 10# 行走速度
    
    def __init__(self) -> None:
        pass
    
    # 绘制脚印
    def draw_feet(self, win : pg.Surface):
        
        ftl = pg.transform.rotate(self.feetl_img, 90)
        ftr = self.feetr_img
        
        win.blit(ftl, [0, 0])
        win.blit(ftr, [12, 0])
    
    # 绘制角色
    # 脚印、声波等
    def draw(self, win : pg.Surface):
        self.draw_feet(win)
