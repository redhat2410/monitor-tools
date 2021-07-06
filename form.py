import cv2
from enum import Enum
import numpy as np
import threading
import time
from color import ColorMap, Color
from font import FontStyle, Font
from point import Point
from size import Size


class Form(object):
    def __init__(self):
        # init array image for opencv
        self.Name = 'Form'
        self.Size = Size(600, 400)
        self.Font = Font()
        self.Color = Color(ColorMap.WHITE)
        self.Frame = np.ones((self.Size.getHeight(), self.Size.getWidth(), 3), dtype= np.uint8) * np.array(self.Color.getColorRGB(), np.uint8)
        self.__thread = threading.Thread(target=self.__update)
    
    def __update(self):
        while True:
            cv2.imshow(self.Name, self.Frame)
            time.sleep(0.01)
            if cv2.waitKey(40) == 27:
                break

    def getName(self):
        return self.Name
    
    def getSize(self):
        return self.Size
    
    def getFont(self):
        return self.Font.getFont()

    def setName(self, name : str):
        self.Name = name
    
    def setSize(self, size : Size):
        self.Size = size
        # update frame
        self.Frame = np.resize(self.Frame, (self.Size.getHeight(), self.Size.getWidth(), 3))
    
    def setWidth(self, width : int):
        self.Size.setWidth(width)
        self.Frame = np.resize(self.Frame, (self.Size.getHeight(), self.Size.getWidth(), 3))

    def setHeight(self, height : int) :
        self.Size.setHeight(height)
        self.Frame = np.resize(self.Frame, (self.Size.getHeight(), self.Size.getWidth(), 3))

    def setFont(self, font : Font):
        self.Font = font

    def setBackgroudColor(self, map : ColorMap):
        tempColor = Color(map)
        # reset frame
        self.Frame = (self.Frame * 0) + 1
        # set new color for Frame
        self.Frame = self.Frame * np.array(tempColor.getColorRGB(), np.uint8)

    def setBackgroudImage(self, path : str):
        pass

    def show(self):
        self.__thread.start()
    
    def close(self):
        pass


class Context(object):
    def __init__(form : Form):
        pass