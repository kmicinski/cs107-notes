# Polymorphism lecture notes

import math

itema = ("clothes", 23.50)
itemb = ("food",    14.40)
itemc = ("health",  13.31)

def item_cost(item):
    pass
    
class ClothesItem:
    def __init__(self,baseCost):
        self.cost = baseCost + baseCost * .18

    def getCost(self):
        return self.cost

class FoodItem:
    def __init__(self,baseCost):
        self.cost = baseCost + baseCost * .04

    def getCost(self):
        return self.cost

class HealthItem:
    def __init__(self,baseCost):
        self.cost = baseCost

    def getCost(self):
        return self.cost

class CarItem:
    def __init__(self,baseCost):
        self.cost = baseCost + baseCost * .12

    def getCost(self):
        return self.cost

def item_cost(item):
    return item.getCost()

# Taken from...
# http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def getName(self):
        return "this animal"

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.getName(), self.getSpecies())

x = Animal("yannis", "giraffe")
print(x)

class Dog(Animal):
    def __init__(self,name):
        self.name = name
        self.species = "canine"

    def getSpecies(self):
        return "foo"

y = Dog("ralph")

print("Rendering y:")
print(y)

print(y.noMethodLikeThis())

# class A:
#     def __init__(self):
#         self.x = 0
#         self.y = 1

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def calculate(self):
#         return self.getX() + self.getY()

# class B(A):
#     def __init__(self):
#         super().__init__()

#     def getX(self):
#         return 2
    
#     def calculate(self):
#         return self.getX() + self.getY()

# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.y = 3
    
#     def getY(self):
#         return 4

# print("Value of calculate on A, B, and C")
# x0 = A()
# x1 = B()
# x2 = C()
# print(x0.calculate())
# print(x1.calculate())
# print(x2.calculate())

# class Foo:
#     def __init__(self):
#         self.x = 0
#         self.y = 1

#     def setX(self,x):
#         raise "you can't do that"

#     def setY(self,y):
#         self.y = y

#     def swap(self):
#         x = self.x
#         self.x = self.y
#         self.y = x

# class Bar:
#     def __init__(self):
#         pass

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width  = width

# def area(o):
#     if (isinstance(o,Circle)):
#         return (o.radius * o.radius * math.pi)
#     elif (isinstance(o,Rectangle)):
#         return o.length * o.width

# print(area(Circle(3)))
