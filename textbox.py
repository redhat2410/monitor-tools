import cv2
import numpy as np
import item
from item import Item

class TextBox(Item):
    def __init__(self):
        Item.__init__(self, 'textbox')
        self.Text       = 'textbox'
        self.Enable     = True
        self.Visible    = True
        self._id        = item.TEXTBOX