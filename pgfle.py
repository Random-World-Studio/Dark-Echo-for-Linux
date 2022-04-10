'''
pygame flow engine
pygame流引擎
这个引擎用刷新流类使pygame中surface的刷新与计算分离
'''
from cProfile import run
from pickle import STOP
import pygame as pg
import threading


class EveHandle:  # 事件handler
    def __init__(self, event_t, handle) -> None:
        self.event_t = event_t
        self.handle = handle

    def getType(self):
        return self.event_t

    def getHandle(self):
        return self.handle


def dummy_terminate():
    pass


class Flow:  # 刷新流

    # states
    STOP = 0
    RUNNING = 1

    fpsctl = pg.time.Clock()
    
    mousep = [0, 0]

    # 参数func一定是一个返回布尔值的函数
    # 最后不定参指定要检测的事件以及事件的handler
    def __init__(self, fps: int, func, terminatefunc=dummy_terminate, *evelist: EveHandle) -> None:
        self.fps = fps  # 帧率
        self.func = func  # 刷新函数
        self.terminatefunc = terminatefunc  # 退出函数
        self.evelist = evelist  # 检测的事件handler表
        self.state = self.STOP  # 设置状态为STOP
    
    def get_mouse(self):
        return self.mousep

    # 刷新流的执行函数
    def run(self):
        b = True
        while b and self.state == self.RUNNING:  # 确认状态标志
            b = self.func()  # 执行刷新函数
            
            self.mousep = pg.mouse.get_pos()
            
            # 接收事件
            for event in pg.event.get():
                if event.type == pg.QUIT:  # 拦截退出事件
                    self.terminatefunc()  # 执行退出前函数
                    exit(0)  # 退出
                for which in self.evelist:  # 检测其他事件
                    if event.type == which.getType():
                        which.getHandle()()  # 如果命中则执行handler

            self.fpsctl.tick(self.fps)  # 保持帧率

    # 启动刷新流
    def start(self):
        self.state = self.RUNNING  # 将状态标志置为RUNNING
        flow = threading.Thread(target=self.run)  # 创建线程
        flow.start()  # 执行线程

    # 停止刷新流
    def stop(self):
        self.terminatefunc()
        self.state = STOP
