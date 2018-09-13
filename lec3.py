from logic import *

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
            head(lst) < e
            return True
        except:
            return False


# Insert element e into a sorted list lst
def insert(lst,e):
    """
    >>> insert([1,3,8,9],4)
    [1, 3, 4, 8, 9]
    """
    precondition(isSorted(lst) and compatibleSort(lst,e))
    return lst


