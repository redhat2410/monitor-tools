from point import Point
import cv2
from font import Font, FontStyle
from size import Size
from color import Color, ColorMap

class Item(object):
    def __init__(self, name : str = 'Item'):
        self.Name = name
        self.Text = ""
        self.Point = Point()
        self.Size = Size()
        self.BackColor = Color(ColorMap.WHITESMOKE)
        self.ForeColor = Color(ColorMap.BLACK)

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

    def getForeColor(self):
        return self.ForeColor.getColorRGB()
