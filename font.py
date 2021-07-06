import cv2
from enum import Enum
from color import Color, ColorMap

class FontStyle(Enum):
    FONT_HERSHEY_SIMPLEX        =   cv2.FONT_HERSHEY_SIMPLEX
    FONT_HERSHEY_PLAIN          =   cv2.FONT_HERSHEY_PLAIN
    FONT_HERSHEY_DUPLEX         =   cv2.FONT_HERSHEY_DUPLEX
    FONT_HERSHEY_COMPLEX        =   cv2.FONT_HERSHEY_COMPLEX
    FONT_HERSHEY_TRIPLEX        =   cv2.FONT_HERSHEY_TRIPLEX
    FONT_HERSHEY_COMPLEX_SMALL  =   cv2.FONT_HERSHEY_COMPLEX_SMALL
    FONT_HERSHEY_SCRIPT_SIMPLEX =   cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    FONT_HERSHEY_SCRIPT_COMPLEX =   cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    FONT_ITALIC                 =   cv2.FONT_HERSHEY_SCRIPT_COMPLEX


class Font(object):
    def __init__(self, style : FontStyle = FontStyle.FONT_HERSHEY_SIMPLEX, size : int = 1, color : ColorMap = ColorMap.BLACK):
        self.style  = style
        self.size   = size
        self.color  = color

    def setFont(self, style : FontStyle):
        self.style  = style

    def setSize(self, size : int):
        self.size = size

    def setFontColor(self, color : Color):
        self.color = color

    def getFont(self):
        return self.style.value
    
    def getFontByName(self):
        return self.style.name

    def getSize(self):
        return self.size

    def getColor(self):
        return self.color 