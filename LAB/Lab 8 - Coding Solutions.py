from ArrayStack import ArrayStack

# Q1, see vitamin q3. Want to keep elements in stack the same
def stack_sum(s):
    if len(s) == 0:
        return 0
    else:
        val = s.pop()
        curr_total = stack_sum(s)
        curr_total += val
        s.push(val)
        return curr_total


# Q1v2
def stack_sum2(s):
    total = 0
    if not s.is_empty():  # len(s) != 0
        val = s.pop()
        total = val + stack_sum2(s)
        s.push(val)
    return total


print("\nTESTING Q1:")
s = ArrayStack()  # stack already sorted
for i in range(9, 0, -1):
    s.push(i)
print(stack_sum(s))
print(stack_sum2(s))


# Q2
def eval_prefix(exp_str):
    operators = '+-*/'
    exp_lst = exp_str.split()
    args_stack = ArrayStack()
    # Iterating from the back to the front
    for i in range(len(exp_lst)-1, -1, -1):
        token = exp_lst[i]
        # If token is an argument (a number)
        if token not in operators:
            args_stack.push(int(token))
        # If token is an operator:
        # this means we have two arguments in our stack already
        else:
            arg1 = args_stack.pop()
            arg2 = args_stack.pop()
            if (token == '+'):
                res = arg1 + arg2
            elif (token == '-'):
                res = arg1 - arg2
            elif (token == '*'):
                res = arg1 * arg2
            else: # token == '/'
                if arg2 == 0:
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)

    return args_stack.pop()

# Another version of solution (left to right)
"""
def eval_prefix_left_to_right(exp_str):
    operators = '+-*/'
    exp_lst = exp_str.split()
    args_stack = ArrayStack()

    for token in exp_lst:
        if token in operators:  # always push operators to stack
            args_stack.push(token)
        else:  # number -> either do calculation or pop from the stack
            token = int(token)

            repeat = False
            # if the top of the stack is a number, pop it and the operator
            # to do the calculation
            # this process may need to be repeated if the top of the stack
            # is still a number
            if not args_stack.is_empty() and type(args_stack.top()) != str:
                repeat = True
            while repeat:
                repeat = False
                left_num = args_stack.pop()  # first digit in calculation
                operator = args_stack.pop()  # operator in calculation
                token = calculate(left_num, token, operator)
                # if top of stack is still a number, repeat the process
                if not args_stack.is_empty() and type(args_stack.top()) != str:
                    repeat = True
            # after calculation is done, push the result to the stack
            args_stack.push(token)
    return args_stack.pop()

def calculate(arg1, arg2, operator):
    if (operator == '+'):
        res = arg1 + arg2
    elif (operator == '-'):
        res = arg1 - arg2
    elif (operator == '*'):
        res = arg1 * arg2
    else: # token == '/'
        if arg2 == 0:
            raise ZeroDivisionError
        else:
            res = arg1 / arg2
    return res
"""

print("\nTESTING Q2:")
print(eval_prefix("1134"))  # edge case, just num
print(eval_prefix(" - + * 16 5 * 8 4 20"))
print(eval_prefix("+ * 5 5 / 10 2"))
print(eval_prefix("+ / - 10 2 4 8"))
print(eval_prefix("+ * 6 3 * 8 4"))
print(eval_prefix("- + * 8 2 4 +  3 6"))
print(eval_prefix("+ + + + 1 2 3 4 5 "))  # edge case, all ops in front, all nums in back

# Q3
'''
the idea is to use the stack to store the int values in reverse order

start from the back because stack reverses the order and it's more efficient to remove from the back than it is from the front
is the last elem a list? if so, pop it and extend it back onto the list
is the last elem an instead? if so, store it into the stack

repeat this until the list is empty
then pop all values from the stack and add them back onto the list

'''


def flatten_lst(lst):
    stack = ArrayStack()

    while len(lst) != 0:
        val = lst.pop()  # get the last value
        if isinstance(val, list):  # is it a list?
            lst.extend(val)  # extend it back

        else:  # it's an int, its already flattened
            stack.push(val)

    while not stack.is_empty():
        lst.append(stack.pop())  # remove the values from the stack and place back into the list


print("\nTESTING Q3:")
lst = [1, [2, 3, 4], [5, [6, [7]], [8, [[9]]]]]
print(lst)
flatten_lst(lst)
print(lst)


# Q4
'''
the idea is to store to have the other stack store the values in descending order
ex stack top <-> bottom

s = [1, 5, 8, 2, 5, 9, 2]

helper = [1] 
helper = [5, 1]     5 > 1
helper = [8, 5, 1]  8 > 5
helper = [8, 5, 1]  2 > 8 is false, store 2 in temp var

put the values from helper back onto stack until temp > helper.top()
helper = [5, 1]
helper = [1] 2 > 1 so we can put the value of temp onto the helper stack now
helper = [2, 1]

repeat this process
heleper = [5, 2, 1]
helper = [8, 5, 2, 1]
... so on 

'''

def stack_sort(s):
    helper = ArrayStack()

    while not s.is_empty():
        temp = s.pop()

        while (not helper.is_empty()) and temp < helper.top():
            s.push(helper.pop()) 

        helper.push(temp)

    while not helper.is_empty():
        s.push(helper.pop())

print("\nTESTING Q4:")
s = ArrayStack()  # stack already sorted, best case O(n)
for i in range(9, 0, -1):
    s.push(i)

s2 = ArrayStack()  # descending order stack, worst case O(n^2)
for i in range(1, 10):
    s2.push(i)

s3 = ArrayStack()
for num in [4, 9, 2, 1, 4, 6, 8, 1, 7, 11, 23, 5, 7]:
    s3.push(num)

print(s.data)
stack_sort(s)
print(s.data)

print(s2.data)
stack_sort(s2)
print(s2.data)

print(s3.data)
stack_sort(s3)
print(s3.data)
