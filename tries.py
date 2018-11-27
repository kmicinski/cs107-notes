# Tries
import time
import sys
from matplotlib import pyplot
from hashtables import *

sys.setrecursionlimit(100000) # python has a recurison depth of <
                              # 1000~. so for the purpose of this
                              # assignment I'm increasing it

# Measure the time of some function f
def measureTime(f):
    t1 = time.time()
    f()
    t2 = time.time()
    return t2 - t1

# Test some function f on a set of inputs. Each of the inputs is a
# tuple (pair) where the first element of the tuple is the argument to
# be passed to `f` (the function to test) and the second element of
# the tuple is the number `n`.
def testEach(f,inputs):
    if (len(inputs) == 0):
        return([],[],[])
    else:
        n = inputs[0][1]
        time = measureTime(lambda : f(inputs[0][0])) * 1000
        space = sys.getsizeof(inputs[0][0])
        print("n = {}, time = {} msec".format(n, time))
        result = testEach(f,inputs[1:])
        return ([n] + result[0], [time] + result[1], [space] + result[2])

def runTests(f,string,inputs):
    print(string)
    results = testEach(f,inputs)
    pyplot.plot(results[0], results[1])
    pyplot.title(string)
    pyplot.xlabel('Hash-Table Size (n)')
    pyplot.ylabel('Time (ms)')
    pyplot.show()
    pyplot.plot(results[0], results[2])
    pyplot.title(string)
    pyplot.xlabel('Hash-Table Size (n)')
    pyplot.ylabel('Memory Usage (Bytes)')
    pyplot.show()

words = []

# Load `words.txt` into a hash table of size s
def loadIntoTable(s):
    print("loading words into table...")
    hashTable = HashTable(s)
    with open("words.txt", "r") as ins:
        for line in ins:
            words.append(line)
            hashTable.insert(line,True)
    return hashTable

# Some input data to run the lists tests on
# inputData = [(loadIntoTable(20000),20000), 
#              (loadIntoTable(40000),40000), 
#              (loadIntoTable(40000),60000), 
#              (loadIntoTable(80000),80000),
#              (loadIntoTable(100000),100000),
#              (loadIntoTable(200000),200000),
#              (loadIntoTable(400000),400000)]

# Look up each word in the hash table
def lookupWords(table):
    print("looking up all words in dictionary")
    for word in words:
        table.lookup(word)

# Test getLast with lists of size 100000, 200000, ...
#print(runTests(lookupWords, "Test of `lookupWords`", inputData))

class Trie:
    def __init__(self, buckets):
        self.content = False
        self.contents = [None] * buckets
        self.buckets = buckets

    def bucket(self,chr):
        return ord(chr) - ord('a')

    def lookupHelper(self,string,i,m):
        if (i >= m):
            return self.content
        else:
            return self.contents[self.bucket(string[i])] != None and self.contents[self.bucket(string[i])].lookupHelper(string,i+1,m)

    def lookup(self,string):
        return self.lookupHelper(string,0,len(string))

    def insertHelper(self,string,i,m):
        if (i >= m):
            # Set this bucket to True
            self.content = True
        else:
            if (self.contents[self.bucket(string[i])] == None):
                self.contents[self.bucket(string[i])] = Trie(self.buckets)
            self.contents[self.bucket(string[i])].insertHelper(string,i+1,m)

    def insert(self,string):
        self.insertHelper(string,0,len(string))

class TwentySixTrie(Trie):
    def __init__(self):
        super(TwentySixTrie, self).__init__(26)

# Some tests..
print("Testing TwentySixTrie")
x = TwentySixTrie()
x.insert("al")
x.insert("ali")
x.insert("aly")
x.insert("allie")
print(x.lookup("ali"))
print(x.lookup("al"))
print(x.lookup("aly"))
print(x.lookup("a"))
print(x.lookup("alo"))
print(x.lookup("allie"))
