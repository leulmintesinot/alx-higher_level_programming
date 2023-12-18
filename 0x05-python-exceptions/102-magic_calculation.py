#!/usr/bin/python3
def magic_calculation(x, y):
    result = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            result += x ** y / i
        except Exception:
            result = y + x
            break
    return result
