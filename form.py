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

class EventType(Enum):
    NO_EVENT                = 0
    EVENT_SINGLE_CLICK      = 1
    EVENT_DOUBLE_CLICK      = 2
    EVENT_RIGHT_MOUSE       = 3
    EVENT_TEXT_CHANGE       = 4
    EVENT_LMOUSE_UP         = 5
    EVENT_LMOUSE_DOWN       = 6
    EVENT_RMOUSE_UP         = 7
    EVENT_RMOUSE_DOWN       = 8

class Form(object):
    def __init__(self):
        # khợi tạo các đối tượng thuộc tính của form
        self.Name = 'Form'
        self.items = list()
        self.Size = Size(600, 400)
        self.Font = Font()
        self.Color = Color(ColorMap.WHITE)
        self.Frame = np.ones((self.Size.getHeight(), self.Size.getWidth(), 3), dtype= np.uint8) * np.array(self.Color.getColorRGB(), np.uint8)
        # tạo luồng xử lý các cập nhật giao của form
        self.__thread = threading.Thread(target=self.__update)
        # khởi tạo môi trường cho update giao diện cho form
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
        # khởi tạo form thừ tham số truyền
        self.form = form
        # khởi tạo các thuộc tính quản lý sự kiện
        self.__previous_event   = EventType.NO_EVENT
        self.__current_event    = EventType.NO_EVENT
        self.__timeout_click    = 0

    def eventUpdate(self):
        cv2.namedWindow(self.form.Name)
        cv2.setMouseCallback(self.form.Name, self.__eventMouse)

    def __eventMouse(self, event, x, y, flags, param):
        retrclick = self.__rightclick(event)
        retdclick = self.__doubleclink(event)

        if retdclick != EventType.NO_EVENT:
            print(retdclick.name)
            self.__ofObject(x, y)

        if retrclick != EventType.NO_EVENT:
            print(retrclick.name)
            self.__ofObject(x, y)

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
        text = txt.getText()
        x, y = txt.getPoint()
        w, h = txt.getSize()
        color = txt.getBackColor()
        bored = txt.getBoredColor()

        x, y = int(x), int(y)
        # draw box for text fill
        cv2.rectangle(self.form.Frame, (x - int(w / 2), y - int(h / 2)), (x + int(w / 2), y + int(h / 2)), color, -1)
        # ve duong vien cho textbox
        cv2.rectangle(self.form.Frame, (x - int(w / 2), y - int(h / 2)), (x + int(w / 2), y + int(h / 2)), bored, 1)
        # fill text for textbox
        cv2.putText(self.form.Frame, text, ((x - int(w / 2)) + 10, (y - int(h / 2)) + 20), txt.Font.getFont(), txt.Font.getSize(), txt.Font.getColor(), 1)

    def __evenMouseManager(self, event : int):
        pass

    def __click(self, event : int):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.__current_event = EventType.EVENT_LMOUSE_DOWN
        elif event == cv2.EVENT_LBUTTONUP and self.__current_event == EventType.EVENT_LMOUSE_DOWN:
            self.__current_event = EventType.NO_EVENT
            return EventType.EVENT_SINGLE_CLICK

        return EventType.NO_EVENT
    def __doubleclink(self, event : int):
        '''
        sự kiện double click là tổ hợp của 2 sử kiện click trong khoảng thời gian ngắn tạo nên
        để phát hiện sự kiện double click cần phải chờ phat hiện 2 sự kiện click trong thời gian
        ngắn
        '''
        if self.__click(event) == EventType.EVENT_SINGLE_CLICK and self.__timeout_click == 0:
            self.__timeout_click = time.perf_counter() * 1000
            return EventType.EVENT_SINGLE_CLICK
        elif self.__timeout_click != 0:
            # kiểm tra thời gian trong 2 lần click phải nhỏ hơn 100 ms thì sẽ chấp nhận sự kiện double click
            if ((time.perf_counter() * 1000) - self.__timeout_click) < 100:
                # reset lại biến timeout
                self.__timeout_click = 0
                return EventType.EVENT_DOUBLE_CLICK
            else:
                self.__timeout_click = 0
        else:
            pass

        return EventType.NO_EVENT

    def __rightclick(self, event : int):
        if event == cv2.EVENT_RBUTTONDOWN:
            self.__current_event = EventType.EVENT_RMOUSE_DOWN
        elif event == cv2.EVENT_RBUTTONUP and self.__current_event == EventType.EVENT_RMOUSE_DOWN:
            self.__current_event = EventType.NO_EVENT
            return EventType.EVENT_RIGHT_MOUSE

        return EventType.NO_EVENT

    def __ofObject(self, _x : int , _y : int):
        for obj in self.form.items:
            # lấy thông tin của đối tượng gồm vị trí và kích thước
            x, y    = obj.getPoint()
            w, h    = obj.getSize()
            
            # thực hiện kiểm tra tọa độ (x, y) thuộc đối tượng nào 
            if ((_x > x) and (_x < (x + w))) and ((_y > y) and (_y < (y + h))):
                print('of ', obj._id)
                return