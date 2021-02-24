##I'm still working on a new tests
import spaghetti_sort
import unittest

class O:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return str(self.x)

class Autotests(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(spaghetti_sort.spaghetti([-3, 3, 1, 2, -1, 4, 0]), [-3, -1, 0, 1, 2, 3, 4]) #test nr 0
        self.assertEqual(spaghetti_sort.spaghetti([1096, 2006, 1004, 1008]), [1004, 1008, 1096, 2006]) #test nr 1
        self.assertEqual(spaghetti_sort.spaghetti([-800, -600, 1100, 900]), [-800, -600, 900, 1100]) #test nr 2
        self.assertEqual(spaghetti_sort.spaghetti([157, 69, 67, 420]), [67, 69, 157, 420]) #test nr 3

    def test_list_with_repeated_elements(self):
        self.assertEqual(spaghetti_sort.spaghetti([54607, -67893, 23674, -30540, -94432, -67893]), [-94432, -67893, -67893, -30540, 23674, 54607]) #test nr 4
        self.assertEqual(spaghetti_sort.spaghetti([67, -63, 64, 67, 64, -63, 65, 65, 64]), [-63, -63, 64, 64, 64, 65, 65, 67, 67]) #test nr 5
        self.assertEqual(spaghetti_sort.spaghetti([0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0]) #test nr 6
        self.assertEqual(spaghetti_sort.spaghetti([81, 81, 78, 78, 78]), [78, 78, 78, 81, 81]) #test nr 7

    def test_list_already_sorted(self):
        self.assertEqual(spaghetti_sort.spaghetti([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) #test nr 8
        self.assertEqual(spaghetti_sort.spaghetti([8, 67, 545, -9063, 34607, -567]), [-9063, -567, 8, 67, 545, 34607]) #test nr 9
        self.assertEqual(spaghetti_sort.spaghetti([14, 14, 14, 14, 14, 14]), [14, 14, 14, 14, 14, 14]) #test nr 10
        self.assertEqual(spaghetti_sort.spaghetti([-78, -78, -81]), [-81, -78, -78]) #test nr 11

    def test_list_sorted_reversed(self):
        self.assertEqual(spaghetti_sort.spaghetti([769003, 12999, 9001, 238, 98, 2, 1, 0]), [0, 1, 2, 98, 238, 9001, 12999, 769003]) #test nr 12
        self.assertEqual(spaghetti_sort.spaghetti([-23098, 23067, -23054, 23045, 23008]), [-23098, -23054, 23008, 23045, 23067]) #test nr 13
        self.assertEqual(spaghetti_sort.spaghetti([697, 586, 475, 364, 253, 142, 31, 2, -1, -901]), [-901, -1, 2, 31, 142, 253, 364, 475, 586, 697]) #test nr 14
        self.assertEqual(spaghetti_sort.spaghetti([8, 6, 4, 2, 0, -2, -4, -6, -8]), [-8, -6, -4, -2, 0, 2, 4, 6, 8]) #test nr 15

    def test_stable(self):
        e1, e2, e3, e4, e5 = O(5), O(8), O(8), O(15), O(8)
        
        self.assertEqual(spaghetti_sort.spaghetti([e4, e2, e3, e1], key = lambda elem: elem.x), [e1, e2, e3, e4]) #test nr 16
        self.assertEqual(spaghetti_sort.spaghetti([e5, e1, e2, e4, e3], key = lambda elem: elem.x), [e1, e5, e2, e3, e4]) #test nr 17
        self.assertEqual(spaghetti_sort.spaghetti([e5, e2, e3], key = lambda elem: elem.x), [e5, e2, e3]) #test nr 18
        self.assertEqual(spaghetti_sort.spaghetti([e4, e2, e1, e5, e1], key = lambda elem: elem.x, descending = True), [e4, e2, e5, e1, e1]) #test nr 19

    def test_descending_order(self):
        self.assertEqual(spaghetti_sort.spaghetti([16208, 16203, -5067, 16205, 16204, -34], descending = True), [16208, 16205, 16204, 16203, -34, -5067]) #test nr 20
        self.assertEqual(spaghetti_sort.spaghetti([91, 23, 145, 130, 145, -6, 13], descending = True), [145, 145, 130, 91, 23, 13, -6]) #test nr 21
        self.assertEqual(spaghetti_sort.spaghetti([-10, -5, -4, -3, -2, -1], descending = True), [-1, -2, -3, -4, -5, -10]) #test nr 22
        self.assertEqual(spaghetti_sort.spaghetti([-3, 3, -3, 4, -4, 4, -4, 4], descending = True), [4, 4, 4, 3, -3, -3, -4, -4]) #test nr 23

    def test_other(self):
        self.assertEqual(spaghetti_sort.spaghetti([]), []) #test nr 24
        self.assertEqual(spaghetti_sort.spaghetti([], descending = True), []) #test nr 25
        self.assertEqual(spaghetti_sort.spaghetti([[9, 'x']], key = lambda elem: elem[0]), [[9, 'x']]) #test nr 26
        self.assertEqual(spaghetti_sort.spaghetti([[9, 'x']], descending = True, key = lambda elem: elem[0]), [[9, 'x']]) #test nr 27

if __name__ == '__main__':
    unittest.main()
