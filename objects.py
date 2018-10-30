class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def getWidth(self): return self.width
    def getHeight(self): return self.height
    def setWidth(self, w): self.width = w
    def setHeight(self, h): self.height = h

    def calculateArea(self):
        return self.getWidth() * self.getHeight()

