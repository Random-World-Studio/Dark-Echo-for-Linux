import sys

sys.stdout = open('./.darkecho.log', 'w')
sys.stderr = open('./.__darkecho.log', 'w')

# 这样做是为了防止格式化程序把这个import放到标准输出重定向之前
if True:
    import pygame as pg

if __name__ == "__main__":
    pg.init()
    pg.display.set_mode([1200, 680])
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)
