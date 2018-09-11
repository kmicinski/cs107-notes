# CS107 Fall '18
# Notes from Thursday, September 6th.
# Run this with:
#     python3 -m doctest 09-06.py
from logic import *

#
# Constructors for lists
# 

# Lists have two basic constructors: 
# - []   -- The empty list
# - cons -- Which appends an element to the front of a list

# Check if a list is empty
def isEmpty(lst):
    """
    >>> isEmpty([])
    True
    
    >>> isEmpty([2,3])
    False
    """
    return lst == []

# Append an element to the front of a list
def cons(head, rest):
    """Construct a list from a head (A) and a rest (list of A)
    
    >>> cons(1,cons(2,cons(3,[])))
    [1, 2, 3]
    """
    # We will expand upon `precondition` in next lecture
    precondition(type(rest)==type([]))
    return [head] + rest

# Get the head of a list
def head(lst):
    """
    >>> head([1,2,3])
    1
    """
    precondition(not isEmpty(lst))
    return lst[0]

# Get the tail of a list
def tail(lst):
    """
    >>> tail([1,2,3])
    [2, 3]
    """
    precondition(type(lst) == type([]))
    return lst[1:]

# Get the length of a list
def length(l):
    """
    >>> length([])
    0
    >>> length([1,2])
    2
    """
    if (isEmpty(l)):
        return 0
    else:
        return 1+(length(tail(l)))

# Get the nth index of a list
def getIndex(l,n):
    """
    >>> getIndex([1,2,3],0)
    1
    
    >>> getIndex([1,2,3],2)
    3
    """
    precondition(type(l) == type([]) and n < len(l))
    if (n == 0):
        return head(l)
    else:
        return getIndex(tail(l),n-1)

# Invert all the signs in a list
def invertSigns(l):
    """
    >>> invertSigns([-3,5,0])
    [3, -5, 0]
    """
    if(isEmpty(l)):
        return []
    else:
        return cons((- head(l)), invertSigns(tail(l)))

# Add one to everything in a list
def addOne(l):
    """
    >>> addOne([-3,5,0])
    [-2, 6, 1]
    """
    if(isEmpty(l)):
        return []
    else:
        return cons(head(l)+1, addOne(tail(l)))

# Multiply everything in the list by 2
def timesTwo(l):
    """
    >>> timesTwo([-3,5,0])
    [-6, 10, 0]
    """
    if(isEmpty(l)):
        return []
    else:
        return cons(head(l)*2, timesTwo(tail(l)))

def timesTwo(n):
    return n*2

# Apply the function f to every element in the list, producing a new
# list
def map(l,f):
    """
    >>> map([-3,5,0], timesTwo)
    [-6, 10, 0]
    """
    precondition(type(l) == type([]))
    if(isEmpty(l)):
        return []
    else:
        return cons(f(head(l)), map(tail(l),f))
