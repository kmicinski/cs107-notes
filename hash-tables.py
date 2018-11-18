#from trees import *

class KeyNotFoundException(Exception):
    pass

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

x = AssocList()
x.insert(1,2)
x.insert(3,4)
x.insert(5,6)
print(x.lookup(5))
print(x.lookup(6))

class HashTable:
    def __init__(self,numBuckets):
        self.buckets = [None] * numBuckets
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets[i] = AssocList()

    def hash(self,key):
        return hash(key) % self.numBuckets

    def insert(self,key,value):
        return

    def lookup(self,key):
        return None

class Dictionary:
    def __init__(self):
        self.tree = None


d = Dictionary()
d.add(1,2)
d.add(3,4)
print(d.lookup(3))
