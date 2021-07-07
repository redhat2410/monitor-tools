from point import Point
from font import Font, FontStyle
from size import Size
from color import Color, ColorMap

DEFAULT =   0
BUTTON  =   1
LABEL   =   2
TEXTBOX =   3

class Item(object):
    def __init__(self, name : str = 'Item'):
        self.Name = name
        self.Text = ""
        self.Point = Point()
        self.Size = Size()
        self.Font = Font()
        self.BackColor = Color(ColorMap.WHITESMOKE)
        self.BoredColor = Color(ColorMap.WHITESMOKE)
        # thuộc tính id dùng để phân loại item là button, label, textbox ...
        # item : 1, 2, 3, ...
        self._id    = DEFAULT

    def setName(self, name : str):
        self.Name = name
    
    def setText(self, text : str):
        self.Text = text

    def setPoint(self, x : int, y : int):
        self.Point = Point(x, y)

    def setSize(self, h : int, w : int):
        self.Size = Size(w, h)

    def setBackColor(self, color : ColorMap):
        self.BackColor = Color(color)

    def setForeColor(self, color : ColorMap):
        self.ForeColor = Color(color)

    def setFont(self, font : Font):
        self.Font = font

    def getName(self):
        return self.Name
    
    def getText(self):
        return self.Text

    def getPoint(self):
        return self.Point.getPoint()

    def getSize(self):
        return self.Size.getSize()

    def getBackColor(self):
        return self.BackColor.getColorRGB()

    def getBoredColor(self):
        return self.BoredColor.getColorRGB()
