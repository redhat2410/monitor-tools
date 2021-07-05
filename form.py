import cv2
from enum import Enum
import numpy as np
import threading
import time

class Point(object):
    def __init__(self, x : int = 0, y : int = 0):
        self.x = x
        self.y = y
    
    def setPoint(self, x : int, y : int):
        self.x = x
        self.y = y

    def getPoint(self):
        return self.x, self.y

    def setX(self, x : int):
        self.x = x
    
    def setY(self, y : int):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

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

class Color(Enum):
    pass

class Font(object):
    def __init__(self, style : FontStyle = FontStyle.FONT_HERSHEY_SIMPLEX, size : int = 1, color : Color = 0):
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
        return self.style

    def getSize(self):
        return self.size

    def getColor(self):
        return self.color 


class Size(object):
    def __init__(self, width : int = 0, height : int = 0):
        self.width      = width
        self.height     = height

    def setWidth(self, width : int):
        self.width      = width

    def setHeight(self, height : int):
        self.height     = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setSize(self, width : int, height : int):
        self.width = width
        self.height = height

    def getSize(self):
        return self.width, self.height

class Form(object):
    def __init__(self):
        # init array image for opencv
        self.Name = 'Form'
        self.Size = Size(600, 400)
        self.Font = Font()
        self.Frame = np.ones((self.Size.getHeight(), self.Size.getWidth(), 3), dtype= np.uint8)
        self.__thread = threading.Thread(target=self.__update)
    
    def __update(self):
        while True:
            cv2.imshow(self.Name, self.Frame)
            # time.sleep(0.01)
            if cv2.waitKey(40) == 27:
                break

    def getName(self):
        return self.Name
    
    def getSize(self):
        return self.Size
    
    def getFont(self):
        return self.Font

    def setName(self, name : str):
        self.Name = name
    
    def setSize(self, size : Size):
        self.Size = size
        # update frame
        self.Frame = np.reshape(self.Frame, (self.Size.getHeight(), self.Size.getWidth(), 3))
    
    def setWidth(self, width : int):
        self.Size.setWidth(width)
        self.Frame = np.reshape(self.Frame, (self.Size.getHeight(), self.Size.getWidth(), 3))

    def setHeight(self, height : int) :
        self.Size.setHeight(height)
        self.Frame = np.reshape(self.Frame, (self.Size.getHeight(), self.Size.getWidth(), 3))

    def setFont(self, font : Font):
        self.Font = font

    def show(self):
        self.__thread.start()
    
    def close(self):
        pass