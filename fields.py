class Example:
    x = 23
    def __init__(self):
        self.foo = 1
        return

    def getFoo(self):
        return self.foo

    def setBar(self):
        self.bar = 1

    def getBar(self):
        return self.bar
    
x = Example().getFoo()
    
