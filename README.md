Cursed spaghetti sort is an implementation for spaghetti sort algorythm.Standard spaghetti sort has a time complexity: O(n),
but it works only theoretically. How it works? Let's assume that for each number from given list, we have uncooked spaghetti 
rod about the height of this number. Now we have to pick them up and press them against the table. Then we can choose
the highest rod and put away to the end of our sorted list. It's very hard to implement, because how to make a table? Or how
computer should recognize a highest rod?

For more information about this algorythm visit:
https://en.wikipedia.org/wiki/Spaghetti_sort
https://www.everything2.com/title/spaghetti+sort

Cursed spaghetti sort does two iterations. First iteration creates a dictionary with next centimeters as a keys and rods as a values
and finds lowest and highest number. In the second iteration, algorythm instead of recognising highest rod, checks every
centimeter between highest and lowest rod and appends rods from current centimeter to the sorted list.

Best time complexity occurs when differences between next sorted elements are zero or one(e.g, [4, 2, 5, 1, 3, 2])

best time complexity: O(n)
average time complexity: O(h - l) where h and l are the biggest and smallest values in the list.
worst time complexity: O(h - l)

Algorythm is stable.

Arguments for this function:
1. list_ - list of integral numbers you want to sort.
spaghetti([7, -2, 1, 0]) -> [-2, 0, 1, 7]

2. descending - when you set it to True, list will be sorted in descending order.
spaghetti([-1, 2, -3, 4], descending = True) -> [4, 2, -1, -3]

3. key - use it when you want to sort a list of objects or tuples.
It requires a function, with only one argument, which will extract interesting value from element.
When sorting list of tuples or lists by first element: spaghetti([(10, -5), [0, 0, "p"], [10, -8], (12, "xxx")], 
key = lambda elem: elem[0]) -> [[0, 0, "p"], (10, -5), [10, -8], (12, "xxx")]
When sorting list of objects by object's attributes: spaghetti([Obj(16), Obj(-6), Obj(6), Obj(4)], key = lambda elem: elem.x) -> [Obj(-6), Obj(4), Obj(6), Obj(16)]

Feel free to use this code where you want, but if it's possible please mark me (https://github.com/kubak14)
