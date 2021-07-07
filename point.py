class Point(object):
    def __init__(self, x : int = 0, y : int = 0):
        self.x = x
        self.y = y
    
    def setPoint(self, x : int, y : int):
        self.x = x
        self.y = y

    def getPoint(self):
        return (self.x, self.y)

    def setX(self, x : int):
        self.x = x
    
    def setY(self, y : int):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y