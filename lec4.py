# Notes from 107, 9-13, Lecture 4
# Run via:
#     python3 -m doctest lec4.py
from logic import *
from lec2 import *

# In this lecture, we covered the following:
#   - Complexity / running time examples
#   - Specifying preconditions
#   - Preconditions vs. tests
#   - A precise precondition for `insert`
#   - A preise postcondition for `insert`

# Predicate to determine if a list is sorted
def isSorted(lst):
    """
    >>> isSorted([])
    True
    >>> isSorted([1])
    True
    >>> isSorted([2,1])
    False
    >>> isSorted([1,2])
    True
    >>> isSorted([3,6,7,-5])
    False
    """
    if (len(lst) == 0 or len(lst) == 1): return True
    if (head(lst) < head(tail(lst))):
        return isSorted(tail(lst))
    else: return False


def gt0(e):
    return e > 0

# Test if the function `prop` returns True for every item of
# the list `lst`.
# Returns true if...
#   for all 0 <= i < len(lst), prop(lst[i]) == True 
def forall(lst,prop):
    """
    >>> forall([1,2], gt0)
    True
    >>> forall([-1,2], gt0)
    False
    """
    if (isEmpty(lst)): return True
    else:
        return prop(head(lst)) and forall(tail(lst),prop)

# Check if a list lst is compatible with being sorted via e's type
# Next lecture we will generalize this to the whole list via 
# forall
def compatibleSort(lst,e):
    """
    >>> compatibleSort([1],1)
    True
    >>> compatibleSort(["a"],1)
    False
    """
    if (isEmpty(lst)): return True
    else:
        try:
            # Note: even if the following expression is false, we will
            # return true as long as the comparison succeeds. In other
            # words, we are only testing this not for the return
            # value, but to ensure that it is *possible* to comapre
            # the two.
            head(lst) < e
            return True
        except:
            return False

# Insert element e into a sorted list lst
# Think about the postcondition here
def insert(lst,e):
    """
    >>> insert([1,3,8,9],4)
    [1, 3, 4, 8, 9]
    """
    precondition(isSorted(lst) and compatibleSort(lst,e))
    return lst
