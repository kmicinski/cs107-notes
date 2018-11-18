import unittest
from hashtables import *

class TestHashTable(unittest.TestCase):
    def test_insertStress(self):
        x = HashTable(43)
        for i in range(20000):
            x.insert(i,i+1)
        for i in range(20000):
            self.assertEqual(i+1, x.lookup(i))

unittest.main()
