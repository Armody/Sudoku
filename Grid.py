from Cell import *

class Grid():
    def __init__(self, x1, y1, cell_size, win=None):
        self._x1 = x1
        self._y1 = y1
        self._cell_size = cell_size
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size
        y1 = self._y1 + j * self._cell_size
        x2 = x1 + self._cell_size
        y2 = y1 + self._cell_size
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
