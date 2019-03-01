"""zwraca tablicę współrzędnych punktów odcinka"""


def get_line(x1, y1, x2, y2):
    x = x1
    y = y1
    step_x = 1
    dx = x2 - x1
    step_y = 1
    dy = y2 - y1
    if x1 > x2:
        step_x = -1
        dx *= -1
    if y1 > y2:
        step_y = -1
        dy *= -1
    pixels=[(x, y)]
    if dx > dy:
        step_a = (dy - dx) * 2
        step_b = dy * 2
        d = step_b - dx
        while x != x2:
            if d >= 0:
                x += step_x
                y += step_y
                d += step_a
            else:
                d += step_b
                x += step_x
            pixels = pixels.append((x, y))
    else:
        step_a = (dx - dy) * 2
        step_b = dx * 2
        d = step_b - dy
        while y != y2:
            if d >= 0:
                x += step_x
                y += step_y
                d += step_a
            else:
                d += step_b
                y += step_y
            pixels = pixels.append((x, y))
    return pixels

