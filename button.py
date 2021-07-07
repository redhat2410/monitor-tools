import cv2
import numpy as np
import item
from item import Item


class Button(Item):
    def __init__(self):
        Item.__init__(self, 'button')
        self.Text       = 'button'
        self.Enable     = True
        self.Visible    = True
        self._id        = item.BUTTON
    
    def handle_click(self, pointer):
        pointer()

    def handle_doubleclick(self, pointer):
        pointer()

