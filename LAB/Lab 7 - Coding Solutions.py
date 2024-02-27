#Lab 7: Recursion Practice w/ Nested Lists


#Question 1
#Write a function that takes in a list with elements from 0 to n-1 
#and sorts them in place
def SortLst(lst):
    i = 0
    while i < len(lst):
        if lst[i] != i:
            j = lst[i]
            lst[i], lst[j] = lst[j], lst[i]
        else:
            i += 1


# QUESTION 2
#Write a function that takes in two strictly increasing lists and returns the 
#intersection of elements between them in a list
def intersectionOfLst(lst1,lst2):
    res = []

    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(lst1) and ptr2 < len(lst2):
        if lst1[ptr1] == lst2[ptr2]:
            res.append(lst1[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif lst1[ptr1] > lst2[ptr2]:
            ptr2 += 1
        else:
            ptr1 += 1
    return res


# QUESTION 3
#Write a recursive function that takes in a non-negative integer n and returns True 
#if it is a power of 2 and False otherwise.
def isPowerOfTwo(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    return isPowerOfTwo(n/2)


# QUESTION 4
# Write a recursive function that takes in a list of integers and mutates it so that
# all the even numbers are at the front and all the odd numbers are in the back.
def split_parity(lst, low, high):
    if low >= high:
        return

    # low has even and high has odd, swap
    if lst[low] % 2 != 0 and lst[high] % 2 == 0:
        lst[low], lst[high] = lst[high], lst[low]
    if lst[low] % 2 == 0: # low has even, move up
        low += 1
    if lst[high] % 2 != 0: # high has odd, move down
        high -=1
    split_parity(lst, low, high)


#QUESTION 5
#Write a recursive function to find the total sum of a nested list of integers. 
def nested_sum(lst):
    if isinstance(lst, int):
        return lst
    else:
        total = 0
        for i in lst:
            total += nested_sum(i)
        return total


#QUESTION 6
def nested_depth_level(lst):
    if isinstance(lst, list):
        return 1 + max(nested_depth_level(elem) for elem in lst)
    else:
        return 0

def nested_depth_level2(lst):  # simple
    return 1 + max(nested_depth_level2(elem) if isinstance(elem, list) else 0 for elem in lst)

lst = [[1, 2], 3, [4, [5, 6, [7], 8]], [[[[9]]]]]
print("\nDepth Level:", nested_depth_level(lst))


#QUESTION 7
#simple modification of reverse by incrementing low -> low + 1, high -> high-1, swap low and high
def deep_reverse(lst, low, high):
    if low > high:
        return

    if isinstance(lst[low], list):
        deep_reverse(lst[low], 0, len(lst[low])-1)

    #the low != high is to ensure that you don't reverse twice, because that will undo the reverse
    #ex) [[1, 2]], we want this to be [[2, 1]] but it will swap twice since low == high == 0
    if low != high and isinstance(lst[high], list): 
        deep_reverse(lst[high], 0, len(lst[high])-1)

    lst[low], lst[high] = lst[high], lst[low] #swap 

    deep_reverse(lst, low+1, high-1) #move low and high closer to each other


lst = [[1], [[2, [3]]], [[[4], 5], 6], 7, 8, [[[[[[9]]]], 10]]]
lst = [[1, 2], 3, [4, [5, 6, [7], 8 ] ], [ [ [ [9] ] ] ]  ]
#lst = [1, [2, 3], 4]
print("Original: ",lst)
deep_reverse(lst, 0, len(lst)-1)
print("Reversed: ",lst)
deep_reverse(lst, 0, len(lst)-1)
print("Reversed Back: ",lst)


#QUESTION 8
def yield_flattened(lst):
    for elem in lst:
        if isinstance(elem, int):
            yield elem
        else:
            yield from yield_flattened(elem)

def yield_flattened2(lst):
    for elem in lst:
        if isinstance(elem, int):
            yield elem
        else:
            for elem in yield_flattened2(elem):
                yield elem

def print_flattened(lst):
    print("[" + ",".join(str(num) for num in yield_flattened(lst))+ "]")

print("\nPrint Flattened:\n")
print("Original: ", lst)
print_flattened(lst)
print("Original: ", lst)
print_flattened(lst)
