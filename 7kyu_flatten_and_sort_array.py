# Problem: 7kyu_Flatten_and_sort_an_array
"""
Challenge:

Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

Addendum:

Please, keep in mind, that JavaScript is by default sorting objects alphabetically. For more information, please consult:

http://stackoverflow.com/questions/6093874/why-doesnt-the-sort-function-of-javascript-work-well
"""

#First Approache:
def flatten_and_sort(array):

    # Empty list
    arr = []
    for l in array:
        arr += l
    return sorted(arr)

# 2nd Approache:

def flatten2(array):
    return sorted([dim2 for dim1 in array for dim2 in dim1])



flatten_and_sort2 = lambda arr: sorted([d2 for d1 in arr for d2 in d1])

# Test Zone:

p = [[3, 2], [4, 6, 5], [], [9, 8]]
l = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
print(flatten_and_sort2(l))