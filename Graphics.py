from tkinter import *
from tkinter import ttk
import tkinter.font
import re

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Sudoku")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill="both", expand=1)
        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__canvas.update_idletasks()
        self.__canvas.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, color="black", width=2):
        line.draw(self.__canvas, color, width)

    def check_num(self, newval):
        return re.match('^[0-9]*$', newval) is not None and len(newval) <= 1

    def create_entry(self, x1, x2, y1, y2):
        _font = tkinter.font.Font(size=int((x2-x1)/1.5))
        entry = ttk.Entry(self.__canvas, 
                          justify=CENTER, 
                          font=_font, 
                          foreground="blue", 
                          width=1, 
                          textvariable=StringVar(), 
                          validate="key", 
                          validatecommand=(self.__canvas.register(self.check_num), "%P"))
        entry.place(height=x2-x1, width=y2-y1, x=x1, y=y1)
        return entry

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, color="black", _width=2):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=_width
        )
