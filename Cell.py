from Graphics import *

class Cell():
    def __init__(self, win=None):
        self.left_border = False
        self.right_border = False
        self.top_border = False
        self.bottom_border = False
        self.value = None
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
        #self._entry = ttk.Entry(win.__root, cursor="icon", width=1)

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        border_width = 3

        self._entry = self._win.create_entry(x1, x2, y1, y2)
        
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.left_border:
            self._win.draw_line(left_wall, "black", border_width)
        else:
            self._win.draw_line(left_wall, "gray")
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.right_border:
            self._win.draw_line(right_wall, "black", border_width)
        else:
            self._win.draw_line(right_wall, "gray")
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.top_border:
            self._win.draw_line(top_wall, "black", border_width)
        else:
            self._win.draw_line(top_wall, "gray")
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.bottom_border:
            self._win.draw_line(bottom_wall, "black", border_width)
        else:
            self._win.draw_line(bottom_wall, "gray")
        