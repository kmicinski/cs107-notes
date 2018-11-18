#from trees import *

class KeyNotFoundException(Exception):
    pass

class Car:
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color

    def __str__(self):
        return "Car make: %s, model: %s (color: %s)" % (self.make, self.model, self.color)

    def clone(self):
        return Car(self.make, self.model, self.color)

class AssocList:
    def __init__(self):
        self.list = []
    
    def insert(self,k,v):
        self.list = [(k,v)] + self.list

    def lookup(self,k):
        for item in self.list:
            if (item[0] == k):
                return item[1]  
        raise KeyNotFoundException()

    def length(self):
        return len(self.list)

    def clone(self):
        x = AssocList()
        x.list = []
        for item in self.list:
            x.list = [(item[0], item[1].clone())] + x.list
        return x

    def __str__(self):
        s = ""
        for item in self.list:
            s += "(%s, %s)\n" % (item[0], item[1])
        return s

x = AssocList()
x.insert("a", Car("ford","fusion","black"))
x.insert("b", Car("mazda","rx8","blue"))
c = x.lookup("a")
c.model = "mustang"
y = x.clone()
y.insert("c", Car("a","b","c"))
print("x is")
print(x)
print("y is")
print(y)
c = y.lookup("a")
c.model = "othermodel..."
print(y)
print(x)

class HashTable:
    def __init__(self,numBuckets):
        self.buckets = [None] * numBuckets
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets[i] = AssocList()

    def hash(self,key):
        return hash(key) % self.numBuckets

    def insert(self,key,value):
        self.buckets[self.hash(key)].insert(key,value)

    def lookup(self,key):
        return self.buckets[self.hash(key)].lookup(key)
        
