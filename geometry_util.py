import math

DIRECTION_LEFT = "left"
DIRECTION_RIGHT = "right"


def vectors_angle(x1, y1, x2, y2):
    x2, y2 = x2 - x1, y2 - y1
    res = x2 / math.sqrt(math.pow(x2, 2) + math.pow(y2, 2))
    res = math.acos(res)
    res *= float(180) / math.pi
    res = round(res, 3)
    if y2 < 0:
        res = -1 * res + 360
    return res


def direction_change(x1, y1, x2, y2, x3, y3):
    a1 = vectors_angle(x1, y1, x2, y2)
    a2 = vectors_angle(x2, y2, x3, y3)

    a1a2 = a2 - a1
    # a2a1 = a1 - a2
    a2a1 = (-1 * a1 + 360) - (-1 * a2 + 360)

    d = a1a2 if abs(a1a2) < abs(a2a1) else a2a1
    return DIRECTION_RIGHT if d > 0 else DIRECTION_LEFT
