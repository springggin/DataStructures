# 1a

"""
Idea: swap the first and last elements, then swap the second and second to last elements, etc.
Approach: 2 pointers, one at front and one at end of the list. Swap and move both pointers inwards.
"""

def reverse(lst):
    low  = 0
    high = len(lst) - 1
    
    while low < high: # stop when the pointers meet in the middle
        lst[low], lst[high] = lst[high], lst[low] # swap
        low += 1
        high -= 1

# compacted version
def reverse2(lst):
    for i in range(len(lst)//2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]

print("------ 1a ------")
lst = [1, 2, 3, 4, 5, 6, 7]
lst2 = [1, 2]
print(f"{lst=}")
reverse(lst)
print(f"{lst=} <- reverse(lst)")
reverse2(lst)
print(f"{lst=} <- reverse2(lst)")

print(f"{lst2=}")
reverse(lst2)
print(f"{lst2=} <- reverse(lst2)")
reverse2(lst2)
print(f"{lst2=} <- reverse2(lst2)")

# 1b
"""
Just add some default parameters to the function.
"""
def reverse_list(lst, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst)-1

    while low < high:
        lst[low], lst[high] = lst[high], lst[low] #swap
        low += 1
        high -= 1

def reverse_list2(lst, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst)

    for i in range(low, high//2):
        lst[i], lst[high - 1 - i] = lst[high - 1 - i], lst[i]


print("------ 1b ------")
lst = [1, 2, 3, 4, 5, 6, 7]
lst2 = [1, 2]

print(f"{lst=}")
reverse_list(lst)
print(f"{lst=} <- reverse_list(lst)")
reverse_list2(lst)
print(f"{lst=} <- reverse_list2(lst)")

print(f"{lst2=}")
reverse_list(lst2)
print(f"{lst2=} <- reverse_list(lst2)")
reverse_list2(lst2)
print(f"{lst2=} <- reverse_list2(lst2)")

#2
def powers_of_two(n):
    for i in range(n):
        yield 2**i


# test:
print("------ 2 ------")
for i in powers_of_two(6):
    print(i, end=" ")
print()

#3
"""
A bit tricky. Your initial idea might be to pop any zero you see and append it to the end of the list.
BUT, this is not O(n) as pop() is not a constant time operation when popping from the middle of a list.

Instead, we'll use another 2 pointer approach.
Keep track of the most left 0. Anytime you see a non-zero, swap it with the most left 0 and move the most left 0 up.
Even if the zero pointer does not point at a zero, it'll just swap and move both pointers up.
"""
def move_zeroes(nums):
    first_possible_zero = 0  # keep track of the most left 0 or non-zero number
    for i in range(len(nums)): #use i to traverse through the list, 
        if nums[i] != 0: #if lst[i] != 0, swap, then move the zero reference up
            nums[i], nums[first_possible_zero] = nums[first_possible_zero], nums[i]
            first_possible_zero += 1

    #this solution also works because if last_zero is actually not referencing a 0 and neither is nums[i], it'll just swap and move BOTH pointers up

#Consider these test cases! 
print("------ 3 ------")
print("Zeroes in between list:")
lst = [1, 0, 0, 13, 0, 3]
print(f"{lst=}")
move_zeroes(lst)
print(f"{lst=} <- move_zeroes(lst)")

print("Zeroes in front of list:")
lst = [0, 0, 0, 1, 13, 3]
print(f"{lst=}")
move_zeroes(lst)
print(f"{lst=} <- move_zeroes(lst)")

print("Zeroes in back of list:")
lst = [1, 13, 3, 0, 0, 0]
print(f"{lst=}")
move_zeroes(lst)
print(f"{lst=} <- move_zeroes(lst)")

print("Shuffle Shuffle:")
import random
length = random.randint(5, 15)
lst = [random.randint(0, 30)*(random.randint(0, 2)) for i in range(length)] 
random.shuffle(lst)
print(f"{lst=}")
move_zeroes(lst)
print(f"{lst=} <- move_zeroes(lst)")


#4
'''
ex) lst = [1, 2, 3, 4, 5, 6], shift(lst, 2) -- > [5, 6, 1, 2, 3, 4]
reverse the whole list --> [6, 5, 4, 3, 2, 1]
reverse the list from 0 to k-1 (2-1 = 1) --> [5, 6, 4, 3, 2, 1]
reverse the list from k=2 to len(lst)-1 --> [5, 6, 1, 2, 3, 4]

ANALYSIS
reverse whole list costs n 
reverse list from 0 to k-1 costs k
reverse list from k to n costs n-k
together n + k + (n-k) = 2n = O(n)
'''
def shift(lst, k):
    reverse_list(lst) #reverse the whole lst
    reverse_list(lst, 0, k-1) #reverse the lst from 0 to k
    reverse_list(lst, k, len(lst)-1) #reverse the lst from k to len(lst)-1

#test
print("------ 4 ------")
lst = [1, 2, 3, 4, 5, 6]
print(f"{lst=}")
shift(lst, 2)
print(f"{lst=} <- shift(lst, 2)")
lst = [1, 2, 3, 4, 5, 6]
print(f"{lst=}")
shift(lst, 5)
print(f"{lst=} <- shift(lst, 5)")
