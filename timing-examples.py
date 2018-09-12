# Algorithmic runtime examples
import time
# Make attractive plots
from matplotlib import pyplot
from memory_profiler import memory_usage
import sys

sys.setrecursionlimit(100000) # python has a recurison depth of < 1000~. so for the purpose of this assignment I'm increasing it

# Measure the time of some function f
def measureTime(f):
    t1 = time.time()
    f()
    t2 = time.time()
    return t2 - t1

# Measure the memory used by `f` (as measured by `memory_profiler`)
def measureSpace(f):
    return memory_usage(f)

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
        space = measureSpace(lambda : f(inputs[0][0]))
        print("n = {}, time = {} msec".format(n, time))
        result = testEach(f,inputs[1:])
        return ([n] + result[0], [time] + result[1], [max(space)] + result[2])

def runTests(f,string,inputs):
    print(string)
    results = testEach(f,inputs)
    pyplot.plot(results[0], results[1])
    pyplot.title(string)
    pyplot.xlabel('Input Size (n)')
    pyplot.ylabel('Time (ms)')
    pyplot.show()
    pyplot.plot(results[0], results[2])
    pyplot.title(string)
    pyplot.xlabel('Input Size (n)')
    pyplot.ylabel('Space (MiB)')
    pyplot.show()
    
# List destructors, regarding arrays as lists
def head(l):
    return l[0]

def tail(l):
    return l[1:]

# Get the last element of the list using primitive destructors on the
# list (rather than it's random-access property)
def getLast(l):
    if (len(l) == 1): return head(l)
    else: return getLast(tail(l))

# Some input data to run the lists tests on
inputData = [([1] * 2000,2000), 
             ([1] * 4000,4000), 
             ([1] * 6000,6000), 
             ([1] * 8000,8000),
             ([1] * 10000,10000)]

# Test getLast with lists of size 100000, 200000, ...
print(runTests(getLast, "Test of `getLast`", inputData))

# Test tail with lists of size 100000, 200000, ...
#print(runTests(tail, "Test of `tail` (l[1:])", inputData))
