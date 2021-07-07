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
        return (self.width, self.height)