COLOR_BLACK = 0
COLOR_WHITE = 1


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def get_point(value):
    if len(str(value)) != 2:
        return None
    col, row = list(value)
    col = ord(str(col).upper())
    row = int(row)
    if 65 <= col <= 72 and 1 <= row <= 8:
        return row - 1, col - 65
    return None
