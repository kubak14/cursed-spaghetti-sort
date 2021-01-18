##author: github.com/kubak14
##best time complexity: O(n)
##average time complexity: O(x - y) where x is the biggest number and y is the smallest number in list
##worst time complexity: O(x - y)
##for more information, please visit README file: github.com/kubak14/REDME

def spaghetti(iterable, key = None, descending = False) -> 'sorted list':
    "Returns sorted list"

    rod_heights = dict()
##  this dictionary holds the heights of successive rods as keys and
##  list of elements with the same height as values
##  (if iterable contains only integers it could be just number
##  of elements with this height as value, but list is neccessary
##  to keep alghorythm stable)
    max_value = 0 #highest rod in the list
    min_value = 0 #shortest rod in the list

    for elem in iterable:
##      in the first iteration we have to find the highest rod
##      and convert list into dictionary
        if key != None:
            v = key(elem) #swapping variable elem with attribute of the elem provided by user
        else:
            v = elem

            
        if v in rod_heights: #if element is already in dictionary
            rod_heights[v].append(elem) #we can add current element to it

        else:
            rod_heights[v] = [elem] #else we have to create it first


        if v > max_value: #checking if the current element is bigger than current biggest value
            max_value = v

        if v < min_value: #checking if the current element is smaller than current smallest value
            min_value = v

    length = len(iterable) #capturing current length of iterable
    iterable.clear() #clearing iterable, so we won't have to create more data structures


    for h in range(max_value, min_value-1, -1):
##      in the second iteration we are going trought all numbers
##      from biggest value to zero and sorting elements up to date
        elem_list = rod_heights.get(h, None) #this variable holds elements under index h(if there is no index h it returns None instead of error)

        if elem_list != None: #if index exist
            iterable = elem_list + iterable if not descending else iterable + elem_list
##          here, we are adding elements to the start or end of iterable depending on arguments sended to function

            if len(iterable) == length:
##              if current length of iterable is equal to length of iterable before clear,
##              it means that iterable is sorted and we can end the program
                break

    return iterable


if __name__ == '__main__':
    print(spaghetti([5, 9, 2, 0, 10, 3, 1, 8, 500, 7, 4, 6, 10]))
