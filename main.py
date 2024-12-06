from Graphics import *
from Grid import *

def main():
    size_x = 800
    size_y = 600
    margin = 50
    cell_size_x = (size_x - margin * 2) / 9
    cell_size_y = (size_y - margin * 2) / 9
    cell_size = min(cell_size_x, cell_size_y)
    win = Window(size_x, size_y)

    grid = Grid(50, 50, cell_size, win)

    win.wait_for_close()

main()