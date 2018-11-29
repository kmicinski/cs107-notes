# Tries
import time
import sys
from matplotlib import pyplot
from hashtables import *

# hash-table based implementation of a set
class Set:
    def __init__(self):
        self.hashtable = HashTable(43)
    
    def insert(self,e):
        self.hashtable.insert(e,True)

    def contains(self,e):
        try:
            self.hashtable.lookup(e)
            # If I got here, I didn't throw an exception
            return True
        except:
            return False

s = Set()
s.insert("dog")
s.insert("cat")
print(s.contains("dog"))
print(s.contains("cat"))
print(s.contains("squirrel"))

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
# print(runTests(lookupWords, "Test of `lookupWords`", inputData))

class Trie:
    def __init__(self, numBuckets, hasContent):
        self.content = hasContent
        self.contents = [None] * numBuckets
        self.buckets = numBuckets

    def bucket(self,chr):
        return ord(chr) - ord('a')

    def __str__(self):
        return ""

    def setBucket(self,character,t):
        self.contents[self.bucket(character)] = t

    def hasBucket(self,character):
        return self.contents[self.bucket(character)] != None

    def hasContent(self): return self.content

    # Return True is string is in the trie (really, the set the trie
    # represents), False otherwise.
    def lookup(self,string):
        """
        >>> t1 = Trie(26, False)
        >>> t2 = Trie(26, True)
        >>> t3 = Trie(26, True)
        >>> t4 = Trie(26, True)
        >>> t1.setBucket('c', t2)
        >>> t2.setBucket('a', t3)
        >>> t1.setBucket('b', t4)
        >>> t1.lookup("c")
        True
        >>> t1.lookup("ca")
        True
        >>> t1.lookup("")
        False
        >>> t1.lookup("car")
        False
        >>> t1.lookup("b")
        True
        """
        # The trie that I'm currently considering
        curTrie = self
        # The character within `string` I'm looking at
        i       = 0
        
        while(i < len(string)):
            if (curTrie.contents[self.bucket(string[i])] != None):
                curTrie = curTrie.contents[self.bucket(string[i])]
            else:
                # I will know that the string I'm looking for can't be
                # in the trie.
                return False
            i = i+1
            
        # curTrie contains the trie represented by the string
        return curTrie.hasContent()

    # Insert a string into the trie at the appropriate location.
    def insert(self,string):
        curTrie = self
        i       = 0

        while(i < len(string)):
            if (curTrie.contents[self.bucket(string[i])] != None):
                curTrie = curTrie.contents[self.bucket(string[i])]
            else:
                # Potentially add necessary new bucket to the trie
                t = Trie(self.buckets, False)
                curTrie.contents[self.bucket(string[i])] = t
                curTrie = t
            i = i+1
            
        # curTrie contains the trie represented by the string
        curTrie.content = True

class TwentySixTrie(Trie):
    def __init__(self):
        super(TwentySixTrie, self).__init__(26, False)

# Some tests..
print("Testing TwentySixTrie")

t1 = Trie(26, False)
t2 = Trie(26, True)
t3 = Trie(26, True)
t1.setBucket('c', t2)
t2.setBucket('a', t3)

# Question: What set does trie t1 represent?

print("Testing trie")
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
