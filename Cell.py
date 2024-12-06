from Graphics import *

class Cell():
    def __init__(self, win=None):
        self.value = None
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

        self._is_box = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        color = "black"
        if self._is_box:
            color = "gray"
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(left_wall, color)
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(right_wall, color)
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(top_wall, color)
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(bottom_wall, color)
        