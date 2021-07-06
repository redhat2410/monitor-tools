import cv2
import numpy as np
from item import Item

class Label(Item):
    def __init__(self):
        Item.__init__(self, 'label')
        self.Text       = 'label'
        self.Enable     = True
        self.Visible    = True
    
    def handle_click(self, pointer):
        pointer(self)

    def handle_doubleclick(self, pointer):
        pointer(self)

    def handle_textchanged(self, pointer):
        pointer(self)