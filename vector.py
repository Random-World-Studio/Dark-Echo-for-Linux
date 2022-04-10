import math

def get_horiz_v(v, length):
    return [v[1] * length / math.sqrt(v[0]*v[0] + v[1]*v[1]), -v[0] * length / math.sqrt(v[0]*v[0] + v[1]*v[1])]


def get_v(v, length):
    if get_mould(v) == 0:
        return [0, 0]
    return [v[0] * length / math.sqrt(v[0]*v[0] + v[1]*v[1]), v[1] * length / math.sqrt(v[0]*v[0] + v[1]*v[1])]


def get_neg_v(v):
    return [-v[0], -v[1]]


def v_add(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]


def v_sub(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1]]

def get_mould(v) -> float:
    return math.sqrt(v[0] * v[0] + v[1] * v[1])
