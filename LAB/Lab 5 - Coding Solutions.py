# Lab 5 Coding Question


import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

#Start Code, except for #g
class ArrayList:

    def __init__(self, iter_collection = None):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1

        #g
        if iter_collection is not None:
            for elem in iter_collection:
                self.append(elem)


    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data[i]
        self.data = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n


#d
    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        
        if (ind < 0):
            ind = self.n + ind
        return self.data[ind]

#d
    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)


    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]




#LAB PORTION

#a

    def __repr__(self):
        return ("[" + ", ".join("'"+val+"'" if isinstance(val, str) else str(val) for val in self) + "]") #the if statement adds ' ' if type is str else convert it to str( )


#b

    def __add__(self, other):
        lst  = ArrayList()
        lst  += self 
        lst  += other
        return lst 

#c

    def __iadd__(self, other):
        self.extend(other)
        return self


#e

    def __mul__(self, scalar): #scalar is a multiplicative constant
        lst = ArrayList()
        for i in range(scalar): #k
            lst.extend(self) #n --> total runtime = k*n

        return lst

#f

    def __rmul__(self, scalar):
        return self * scalar


#h 
    def remove(self, val):
        #first find the index at which  arr[i] == val
        i = 0

        #while index is in range and elem at index i isn't val
        while i < self.n and self[i] != val:
            i += 1
        
        while i < self.n - 1:
            self[i] = self[i + 1]
            i += 1
        
        if i < self.n: #i should be in the last index (len - 1). The condition is if i is still within range/ list is not empty.
            self[i] = None
            self.n -= 1

    
#i 
    #we've actually done this before with move_zeroes in Lab 3
    def removeAll(self, val):

        #first move all instances of val to the back
        last_val = 0                   #keep track of the last zero
        for i in range(len(self)):      #use i to traverse through the list, 
            if self[i] != val:            #if lst[i] != 0, swap, then move the last zero reference up
                self[i], self[last_val] = self[last_val], self[i]
                last_val += 1

        while self[i] == val:
           self[i] = None
           i -= 1
           self.n -= 1 #don't forget to decrement the size

'''

arr = ArrayList("Python")
print(arr)


for i in range(len(arr)):
    print(arr[i], end = " ")
    arr[i] *= 2

print( )
for i in range(-1, -len(arr)-1, -1):
    print(arr[i], end = " ")

print()
arr += ArrayList(("Python"))
print(arr)

for i in range(-1, -len(arr)-1, -1):
    print(arr[i])


arr = ArrayList([1, 2, 3, 2, 3, 4, 2, 2])
arr.removeAll(2)
print(arr, len(arr))

arr.removeAll(3)
print(arr, len(arr))

arr.removeAll(5)
print(arr, len(arr))

arr = ArrayList([1, 2, 3, 2, 3, 4, 2, 2])
arr.remove(4)
print(arr, len(arr))

arr.remove(3)
print(arr, len(arr))

arr.removeAll(2)
print(arr, len(arr))

arr += [5, 5, 5]
print(arr, len(arr))
print(arr * 3)
'''

#Q2 Part A
def find_pivot(lst):
    left = 0
    right = len(lst) - 1
    mid = left

    while left < right:
        mid = (left + right)//2
        if (lst[mid] > lst[right]): #if the right bound is smaller than the mid, this part is not sorted
            left = mid + 1 #only increment left, because the smallest should be on the left side
        else: #lst[mid] < lst[left] left bound biger than mid, this part is not sorted
            right = mid
    return left

#Q2 Part B
def shift_binary_search(lst, target):
    mid = find_pivot(lst) #save the pivot
    left = 0
    right = len(lst) - 1

    #ex) [left ... mid] [mid ... right] pivot is the mid; find out which part of the list to search in
    if lst[mid] <= target <= lst[right]: #if in [mid ... right] --> left is mid
        left = mid
    else: #else in [left ... mid] --> right is mid
        right = mid
    #now binary search
    while left <= right:
        mid = (left + right) //2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else: #lst[mid] > target
            right = mid - 1
    return None #couldn't find





#Q3
import math


def jump_search_k(lst, val, k):

    if len(lst) == 0: #check if list not empty first
        return None
    
    curr = 0
    prev = curr #save the prev jump point
    jump = k #how much you jump, this is your k

    #jump not out of bound and lst[curr] < val
    while curr < len(lst) and lst[curr] < val:
        prev = curr
        curr += jump
    #if jump out of range for a non perfect square size
    if curr >= len(lst):
        prev = curr - jump #jump back to prev
        curr = len(lst) - 1 #change upper bound to last index
    #linear search back at most n//k values
    while curr >= prev:
        if lst[curr] == val:
            return curr
        curr -= 1
    return None #couldn't find it


def jump_search(lst, val):

    if len(lst) == 0: #check if list not empty first
        return None
    
    curr = 0
    prev = curr #save the prev jump point
    jump = math.floor(math.sqrt(len(lst))) #how much you jump, this is your k
    #int( len(lst) ** (0.5) )
    #jump not out of bound and lst[curr] < val
    while curr < len(lst) and lst[curr] < val:
        prev = curr
        curr += jump

    #if jump out of range for a non perfect square size
    if curr >= len(lst):
        prev = curr - jump
        curr = len(lst) - 1 #change upper bound to last index

    #linear search back at most sqrt(n) values, k == sqrt(n)
    while curr >= prev:
        if lst[curr] == val:
            return curr
        curr -= 1
    return None #couldn't find it



#Q4
def exponential_search(lst, val):

    if len(lst) == 0: #check if list is not empty
        return None
    
    if lst[0] == val: #check index 0 first
        return 0
    else:
        i = 1 #start at 1 for the exponential search
    while i * 2 < len(lst) and lst[i] < val:
        i *= 2
    left = i//2
    right = i
    if lst[right] < val: #check if out of bounds (exited because i * 2 < len(lst))
        right = len(lst) - 1
    
    #now binary search
    while left <= right:
        mid = (left + right)//2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            left = mid + 1
        elif lst[mid] > val:
            right = mid - 1

    return None
