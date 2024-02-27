"""
1134 Lab 4 - Coding Solutions
Fall 2023
"""

# 1
"""
2 pointers - moving inwards
Compare letters at both pointers, if they match continue moving inwards.
Otherwise, no longer a palindrome and return False.
"""
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# compacted by calculating pointer using other pointer
def is_palindrome2(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1 - i]: #or s[-1 - i]
            return False
    return True

# 2
"""
2 pointers - 2 pointers moving inwards
Very similar to the is_palindrome question. The only difference is that we need to check if the letters are vowels.
If both are vowels, swap them. Otherwise, if not a vowel, move the pointer inwards.
"""
def reverse_vowels(input_str):
    left = 0
    right = len(input_str) - 1
    vowels = 'aeiou'
    lst = list(input_str) # convert string to list - linear operation
    
    while left < right: # can't use for loop because you don't know where vowels are placed
        if lst[left] in vowels and lst[right] in vowels:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

        # Note: 2 separate if statements instead of elif because we want to move both pointers
        # inwards if both letters are not vowels
        if lst[left] not in vowels:
            left += 1

        if lst[right] not in vowels:
            right -= 1

    return "".join(lst) # join list into single string - linear operation

# 3
# a.Brute force solution --> O(n*k)
"""
Calculate the sum for all possible subarrays of size k. Return the maximum sum.
"""
def findMaxSum(nums, k):
    max_sum = 0
    size = len(nums) // k
    for i in range(len(nums) - k + 1):
        curr_sum = 0.0  # find next subarray sum

        for j in range(i, i + k): # O(k) - get subarray sum
            curr_sum += nums[j]

        max_sum = max(max_sum, curr_sum)  # update max_sum

    return max_sum

#b.Sliding window solution --> O(n)
"""
Idea is to not repeat work that was already done. Instead of recalculating the entire subarray sum for
every possible subarray, notice that for a given subarray of size k, the next subarray of size k has the
exact same numbers in its sum, except the first and last elements. These two elements can be tracked using
2 pointers. This approach is called a sliding window where the elements we are considering is a moving window.
We slide the window by moving both pointers up by 1.
"""
def findMaxSum(nums, k):
    start = 0
    end = start

    curr_sum = nums[start]
    curr_max = 0
    # Accumulate the sum of the first k elements
    while (end < round(len(nums) / k) - 1):
        end += 1
        curr_sum += nums[end]

    # Set the max
    curr_max = curr_sum

    # Slide the window
    while (end < len(nums) - 1 ):
        curr_sum -= nums[start] # subtract the first element of the previous subarray
        start += 1
        end += 1
        curr_sum += nums[end] # add the last element of the new subarray
        curr_max = max(curr_max, curr_sum) # update max_sum
    return curr_max

# 4
# 4.a
"""
O(n^2) runtime due to use of 'in' operator. 'in' does a linear search through the list to find the element.
Thus, the runtime is O(n) and we are doing this n times, so O(n^2).
"""

# 4.b
def find_missingb(lst):
    """
    The key idea is that the missing value is the first index i where
    lst[i] != i. We will binary search for this index.

    Furthermore, if lst[i] != i, then lst[j] != j for all j > i.
    i.e. once the index and the value don't correspond, they will never correspond again

    (If you are not convinced of this fact, try some examples)

    Thus, if we check whether middle value has this property, we can adjust the range accordingly.
    """
    left = 0
    right = len(lst) - 1

    # Edge cases: first num missing
    if len(lst) == 0:
        return 0
    # last num missing
    if lst[right] == right: #if lst[right] == right, there is no index where lst[i] != i. Thus, the missing value is the length of the list itself
        return len(lst)

    while left < right:
        mid = (left + right) // 2 # get middle index
        if lst[mid] != mid:
            right = mid
            """
            Note that we need to keep recursing. If lst[mid] = mid, we don't know for sure if mid is the first index
            where this is not true. We just know that the first one must be to the left of mid.
            """
        else:
            left = mid + 1
            """
            mid is for sure not the index we are looking for, so left becomes mid + 1, not just mid.
            We always want to be searching a valid range
            """

    return left # or right, as when the loop breaks, left == right (because we are always searching a valid range)

# 4.c
def find_missingc(lst):
    """
    If all the numbers between 0 and n were present, the sum of the elements of the list would be
    0 + 1 + 2 + 3 + .... + n = n(n+1)/2

    But, somewhere, an element is missing. The sum of the list is thus
    0 + 1 + 2 + 3 + ... + (i - 1) + (i + 1) + ... + n

    If we subtract these two quantities, we find the missing number i.
    """
    n = len(lst)

    expected_sum = n*(n+1)//2
    actual_sum   = sum(lst)
    missing_num  = expected_sum - actual_sum

    return missing_num
