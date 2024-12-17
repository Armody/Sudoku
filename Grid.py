from Box import *

class Grid():
    def __init__(self, x1, y1, cell_size, win=None):
        self._x1 = x1
        self._y1 = y1
        self._cell_size = cell_size
        self._win = win

        self._create_boxes()

    def _create_boxes(self):
        self._boxes = [[Box(self._x1 + i * self._cell_size * 3, 
                            self._y1 + j * self._cell_size * 3,
                            self._cell_size,
                            self._win) for j in range(3)] for i in range(3)]
