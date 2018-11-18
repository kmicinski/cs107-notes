# Review / Warmup

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width * self.height

    def setHeight(self,height):
        self.height = height

    def setWidth(self,width):
        self.width = width
    
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

def useRectangle():
    rectangleA = Rectangle(8,12)
    rectangleB = Rectangle(4,4)
    rectangleA.calculateArea()
    rectangleB.calculateArea()

class CachedAreaRectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cachedArea = width * height

    def calculateArea(self):
        return self.cachedArea

    def setHeight(self,height):
        self.height = height
        self.cachedArea = self.width * height

    def setWidth(self,width):
        self.width = width
        self.cachedArea = width * self.height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

import math

class Circle:
    def __init__(self,x,y,radius):
        self.centerX = x
        self.centerY = y
        self.radius  = radius

    def calculateArea(self):
        return self.radius * self.radius * math.pi










class ShapeList:
    def __init__(self):
        self.list = []
    
    def length(self):
        return len(self.list)

    def add(self,shape):
        self.list = [shape] + self.list
    
    def sumOfAreas(self):
        x = 0
        for shape in self.list:
            x += shape.calculateArea()
        return x

x = ShapeList()
x.add(Circle(2,3,5))
x.add(CachedAreaRectangle(2,3))
x.add(Rectangle(2,3))
print("sum of areas:")
print(x.sumOfAreas())

class Link:
    def __init__(self,data,nextLink):
        self.data = data
        self.nextLink = nextLink
    
    def getData(self): return self.data
    def getNext(self): return self.nextLink
    def hasNext(self): return self.nextLink != None
    def setNext(self, n): self.nextLink = n

l1 = Link("Hello", None)
l2 = Link(23, l1)
l3 = Link(-12,l2)
l4 = Link(17, l3)









class List:
    def __init__(self):
        self.first = None
    
    def add(self, data):
        self.first = Link(data, self.first)
    
    # Delete a piece of data from a list
    def delete(self, data):
        prev = None
        cur  = self.first
        while (cur != None):
            if (cur.getData() == data):
                # Delete this link
                if (prev == None):
                    # Deleting the first link
                    self.first = cur.getNext()
                else:
                    # Deleting a link other than the first
                    prev.setNext(cur.getNext())
            prev = cur
            cur  = cur.getNext()

    def reverse(self):
        rev = None
        cur = self.first
        while (cur != None):
            rev = Link(cur.getData(), rev)
            cur = cur.getNext()
        self.first = rev

    def contains(self, data):
        node = self.first
        while (node != None):
            if (node.data == data): return True
            node = node.next
        return False

x = List()
x.add(2)
x.add(3)
x.add(7)
print(x.contains(3))
print(x.contains(5))
print(x.contains(7))

