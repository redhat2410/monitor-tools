import cv2
import numpy as np
from item import Item, FontStyle, Font, ColorMap, Color, Size, Point


class Button(Item):
    def __init__(self):
        Item.__init__(self, 'button')
        self.Text       = 'button'
        self.Enable     = True
        self.Visible    = True
    
    def handle_click(self, pointer):
        pointer()

    def handle_doubleclick(self, pointer):
        pointer()

