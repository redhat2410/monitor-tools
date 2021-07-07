import item
import cv2
from enum import Enum
import numpy as np
import threading
import time
from color import ColorMap, Color
from font import FontStyle, Font
from point import Point
from size import Size
from item import Item


class Form(object):
    def __init__(self):
        # init array image for opencv
        self.Name = 'Form'
        self.items = list()
        self.Size = Size(600, 400)
        self.Font = Font()
        self.Color = Color(ColorMap.WHITE)
        self.Frame = np.ones((self.Size.getHeight(), self.Size.getWidth(), 3), dtype= np.uint8) * np.array(self.Color.getColorRGB(), np.uint8)
        self.__thread = threading.Thread(target=self.__update)
        self.__context = Context(self)
    
    def __update(self):
        self.__context.eventUpdate()
        while True:
            self.__context.updateFrame()
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

    def Add(self, item : Item):
        self.items.append(item)


class Context(object):
    def __init__(self, form : Form):
        self.form = form

    def eventUpdate(self):
        cv2.namedWindow(self.form.Name)
        cv2.setMouseCallback(self.form.Name, self.__eventMouse)

    def __eventMouse(self, event, x, y, flags, param):
        # if event == cv2.EVENT_LBUTTONDOWN:
        #     cv2.circle(self.form.Frame, (x, y), 3, (0, 0, 255), -1)
        pass

    def updateFrame(self):
        self.__createItems()

    def __createItems(self):
        # khởi tạo đối tượng dựa vào các thuộc tính của item như vị trí, kịch thước, màu, text của đối tượng
        for obj in self.form.items:
            if obj._id == item.BUTTON:
                self.__drawButton(obj)
            elif obj._id == item.LABEL:
                self.__drawLabel(obj)
            elif obj._id == item.TEXTBOX:
                self.__drawTextbox(obj)
            else:
                pass

    def __drawButton(self, btn : Item):
        text = btn.getText()
        x, y = btn.getPoint()
        w, h = btn.getSize()
        color = btn.getBackColor()
        bored = btn.getBoredColor()
        x, y = int(x), int(y)
        # draw button with point, size
        cv2.rectangle(self.form.Frame, (x - int(w / 2), y - int(h / 2)), (x + int(w / 2), y + int(h / 2)), color, -1)
        # draw bored for button
        cv2.rectangle(self.form.Frame, (x - int(w / 2), y - int(h / 2)), (x + int(w / 2), y + int(h / 2)), bored, 1)
        # fill text for button
        cv2.putText(self.form.Frame, text, ((x - int(w / 2)) + 10, (y - int(h / 2)) + 20), btn.Font.getFont(), btn.Font.getSize(), btn.Font.getColor(), 1)

    def __drawLabel(self, lbl : Item):
        text = lbl.getText()
        x, y = lbl.getPoint()
        # w, h = lbl.getSize()
        color = lbl.getBackColor()
        bored = lbl.getBoredColor()

        x, y = int(x), int(y)
        # text for label
        cv2.putText(self.form.Frame, text, (x, y), lbl.Font.getFont(), lbl.Font.getSize(), lbl.Font.getColor(), 1)

    def __drawTextbox(self, txt : Item):
        pass