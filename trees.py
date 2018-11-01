
# Just a function, not method
# Helper function for min
def min2(x,y):
    if (x == None and y != None):
        return y
    elif (y == None and x != None):
        return x
    elif (x == None and y == None):
        return None
    elif (x < y):
        return x
    else:
        return y

# Just a function, not method
# Helper function for min
def max2(x,y):
    if (x == None and y != None):
        return y
    elif (y == None and x != None):
        return x
    elif (x == None and y == None):
        return None
    elif (x > y):
        return x
    else:
        return y

class BinaryTree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    # Print out the contents of every element of the tree using 
    # a preorder traversal
    def render(self):
        print(self.data)
        if (self.left != None):
            self.left.render()
        if (self.right != None):
            self.right.render()

    def lookup(self, data):
        if (self.data == data): return True
        else:
            if (self.left != None):
                if (self.left.lookup(data)): return True
            if (self.right != None):
                if (self.right.lookup(data)): return True
        return False

    # Assume tree might not be sorted
    def min(self):
        lmin = None
        rmin = None
        if (self.left != None):
            lmin = self.left.min()
        if (self.right != None):
            rmin = self.right.min()
        return min2(self.data, min2(lmin, rmin))

    # Assume tree might not be sorted
    def max(self):
        lmin = None
        rmin = None
        if (self.left != None):
            lmin = self.left.min()
        if (self.right != None):
            rmin = self.right.min()
        return max2(self.data, max2(lmin, rmin))

    def isSorted(self):
        lmax = None
        rmin = None
        if (self.left != None):
            lmax = self.left.max()
        if (self.right != None):
            rmin = self.right.min()

        # Something on the left is bigger than the current element
        if (lmin != None and lmax >= self.data):
            return False

        # Something on the right is smaller than the current element
        if (rmin != None and rmax <= self.data):
            return False

        return True

    # def insert(self, data):
    #     return

    # def toArray(self):
    #     return

    def imperativeMap(self,f):
        self.data = f(self.data)
        if (self.left != None):
            self.left.imperativeMap(f)
        if (self.right != None):
            self.right.imperativeMap(f)

    def imperativeMap(self,f):
        self.data = f(self.data)
        if (self.left != None):
            self.left.imperativeMap(f)
        if (self.right != None):
            self.right.imperativeMap(f)

    def persistentMap(self,f):
        left = None
        if (self.left != None):
            # Returns us a copy of left with f mapped over it
            left = self.left.persistentMap(f)
        right = None
        if (self.right != None):
            # Returns us a copy of left with f mapped over it
            right = self.right.persistentMap(f)
        return BinaryTree(f(self.data), left, right)


    # Returns True if data in the tree, False otherwise
    # Assume that this is a sorted binary tree
    def lookupSorted(self,data):
        if (self.data == data): return True
        elif (data < self.data):
            # Go down left branch
            if (self.left != None):
                return self.left.lookup(data)
            else:
                return False
        else:
            # Go down right branch
            if (self.right != None):
                return self.right.lookup(data)
            else: return False

print("t")
t = BinaryTree(13, 
               BinaryTree(25, None, None),
               BinaryTree(16, BinaryTree(12, None, None), None))
t.render()
print("Smallest element in t:")
print(t.min())
print("lookup 25 in t:")
print(t.lookup(25))
print("lookupSorted 25 in t:")
print(t.lookupSorted(25))
t2 = BinaryTree(13, 
               BinaryTree(12, None, None),
               BinaryTree(16, None, BinaryTree(25, None, None)))
print("lookupSorted 25 in t2:")
print(t2.lookupSorted(25))
