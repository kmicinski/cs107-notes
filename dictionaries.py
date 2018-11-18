class Link:
    def __init__(self,data,nextLink):
        self.data = data
        self.nextLink = nextLink
    
    def getData(self): return self.data
    def getNext(self): return self.nextLink
    def hasNext(self): return self.nextLink != None
    def setNext(self, n): self.nextLink = n

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

class ListDictionary:
    def __init__(self):
        self.list = List()

    def set(self,key,value):
        self.add((key, value))
    
    def get(self,key):
        return "not sure"

class LambdaDictionary:
    def __init__(self):
        self.f = (lambda key: 1/0)

    def get(self,data):
        return self.f(data)

    def set(self,key,value):
        self.f = (lambda k:
                  value if k == key else self.f(key))
        
d = LambdaDictionary()
d.set(1,3)
print(d.get(1))
d.set(1,4)
print(d.get(1))

