from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
from TreeHelper import create_lbt_from_list, display_tree


# Create some trees to test with
complete_tree1 = create_lbt_from_list([x for x in range(7)])
complete_tree2 = create_lbt_from_list([x for x in range(15)])
full_tree = create_lbt_from_list([1, 2, 5, 4, 5, 9, 9, 7, 6, 10, 10, None, None, 19, 13, None, None, 4, 1, None, None, None, None, None, None, None, None, 8, 8])
example_tree = create_lbt_from_list([1, 2, 5, 4, 5, None, 9, 7, 6, None, 10, None, None, 19, 13, None, None, 4, 1, None, None, None, None, 8])

print("Complete Tree1:")
display_tree(complete_tree1.root)

print("Complete Tree2:")
display_tree(complete_tree2.root)

print("Full Tree:")
display_tree(full_tree.root)

print("Example Tree:")
display_tree(example_tree.root)


"""
LAB ANSWERS BEGIN HERE.
"""


#QUESTION 1
print("\n\n\nQUESTION 1: Preorder with Stack")

"""
Idea: Mimic recursive call stack with a stack data structure
      Need to push nodes onto the stack in the correct order
"""
#THIS METHOD WAS WRITTEN WITHOUT "self"
def preorder_with_stack(tree):
    """Return a generator that yields the preorder traversal of the tree without recursion."""
    if (tree.root is not None): #the binary tree is not empty
        node = tree.root
        
        s = ArrayStack()
        s.push(node)
        
        while (not s.is_empty()):
            node = s.pop()
            yield node.data

            """
            Preorder is D L R
            the Right Node must go in before the Left Node
            because the stack reverses the order they come out of
            
            """

            if (node.right is not None):
                s.push(node.right)
            
            if (node.left is not None):
                s.push(node.left)




print("\n\nExample Complete Tree1:\n\n", complete_tree1, "\nPreorder:")
for item in preorder_with_stack(complete_tree1):
    print(item, end = ' ')
print()


print("\n\nExample Complete Tree2:\n\n", complete_tree2, "\nPreorder:")
for item in preorder_with_stack(complete_tree2):
    print(item, end = ' ')
print()


print("\n\nExample non Complete Tree:\n\n", example_tree, "\nPreorder:")
for item in preorder_with_stack(example_tree):
    print(item, end = ' ')
print()


print("\n\nExample Full Tree\n\n", full_tree, "\nPreorder:")
for item in preorder_with_stack(full_tree):
    print(item, end = ' ')
print()



#QUESTION 2
print("\n\n\nQUESTION 2: Is Perfect Binary Trees?")
"""
Idea: A perfect binary tree is a binary tree in which all interior nodes have two children and all leaves have the same depth or same level.
      So check each node's children and see if they are a perfect binary tree, and also get their height.
        If the left and right children are both perfect binary trees and have the same height, then the current node is a perfect perfect  tree.
        If the left and right children are both perfect binary trees and have different heights, then the current node is not a perfect binary tree.
        If the left and right children are not both perfect binary trees, then the current node is not a perfect binary tree. 
"""
def is_perfect_recursive(root):
    """Check if a binary tree is perfect recursively"""
    if root is None: # None node is a perfect tree and has height of -1
        return (True, -1)

    left  = is_perfect_recursive(root.left)   # ( bool -> is perfect tree?, height -> integer of height)
    right = is_perfect_recursive(root.right)  # ( bool -> is perfect tree?, height -> integer of height)

    return (left[0] and right[0] and left[1] == right[1], min(left[1], right[1]) + 1)

print("Is Complete Tree1 perfect? :", is_perfect_recursive(complete_tree1.root)[0])

print("Is Complete Tree2 perfect? :", is_perfect_recursive(complete_tree2.root)[0])

print("Is full_tree perfect? :", is_perfect_recursive(full_tree.root)[0])

print("Is example_tree perfect? :", is_perfect_recursive(example_tree.root)[0])


"""Idea: each level should have 2**lvl nodes"""
def is_perfect_iterative(root):
    """Check if a binary tree is perfect iteratively""" 
    q = ArrayQueue()
    q.enqueue(root)
    lvl = 0
    while not q.is_empty():
        if len(q) != 2**lvl:  # Number nodes matches level
            return False
        for _ in range(len(q)):  # for each node in the level
            node = q.dequeue()

            if node.left:
                q.enqueue(node.left)

            if node.right:
                q.enqueue(node.right)
        lvl += 1

    return True


print("Is Complete Tree1 perfect? :", is_perfect_iterative(complete_tree1.root))

print("Is Complete Tree2 perfect? :", is_perfect_iterative(complete_tree2.root))

print("Is full_tree perfect? :", is_perfect_iterative(full_tree.root))

print("Is example_tree perfect? :", is_perfect_iterative(example_tree.root)) 


#QUESTION 3
print("\n\n\nQUESTION 3: Invert Binary Trees")

"""Idea: Recursively invert the left and right subtrees of each node."""
def invert_bt_recursive(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left
    invert_bt_recursive(root.left)
    invert_bt_recursive(root.right)

    """
    Question: what is the differnce between these 3? What effect does it have on the overall function?
     1. root.left, root.right = root.right, root.left
        invert_bt_recursive(root.left)
        invert_bt_recursive(root.right)
     2. invert_bt_recursive(root.left)
        invert_bt_recursive(root.right)
        root.left, root.right = root.right, root.left
     3. invert_bt_recursive(root.left)
        root.left, root.right = root.right, root.left
        invert_bt_recursive(root.right)
    """

def display_tree_and_invert_recursively(tree):
    print("Before recursive invert:")
    display_tree(tree.root)
    invert_bt_recursive(tree.root)
    print("After recursive invert:")
    display_tree(tree.root)
    print()

for tree in [complete_tree1, complete_tree2, full_tree, example_tree]:
    display_tree_and_invert_recursively(tree)



"""Idea: Traverse the tree level by level and invert the left and right subtrees of each node."""
def invert_bt_iterative(root):
    
    q = ArrayQueue()
    q.enqueue(root)
    
    while not q.is_empty():
        for _ in range(len(q)):
            node = q.dequeue()
            node.left, node.right = node.right, node.left # swap nodes
            # add children to queue
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    return root

def display_tree_and_invert_iteratively(tree):
    print("Before iterative invert:")
    display_tree(tree.root)
    invert_bt_iterative(tree.root)
    print("After iterative invert:")
    display_tree(tree.root)
    print()

for tree in [complete_tree1, complete_tree2, full_tree, example_tree]:
    display_tree_and_invert_iteratively(tree)


#QUESTION 4
print("\n\n\nQUESTION 4: Merge Binary Trees")

"""
Idea: Recursively merge the left and right subtrees of each node.
"""
def merge(t1, t2):
    if not t1 and not t2:
        return None

    if t1 and t2: #same as writing if t1 is not None and t2 is not None
        left  = merge(t1.left, t2.left)
        right = merge(t1.right, t2.right)
        t3 = LinkedBinaryTree.Node(t1.data + t2.data, left, right)
        return t3

    if t1: #and not t2; same as writing if t1 is not None and t2 is None
        left  = merge(t1.left, None)
        right = merge(t1.right, None)
        t3 = LinkedBinaryTree.Node(t1.data, left, right)
        return t3

    if t2: #and not t1; same as writing if t2 is not None and t1 is None
        left  = merge(None, t2.left)
        right = merge(None, t2.right)
        t3 = LinkedBinaryTree.Node(t2.data, left, right)
        return t3


def merge_bt(root1, root2):
    root = merge(root1, root2) #you couldve just kept it as one function but this just shows that 
    return root                #merge will always return the root of two subtrees,
                               #with the main root being returned at the end of the recursive function


print("\nExample Tree 1:\n", example_tree)
print("\nExample Tree 2:\n", complete_tree1)
merged_tree = LinkedBinaryTree(merge_bt(example_tree.root, complete_tree1.root))
print("\nMerged Tree (Example Tree 1 + Example Tree 2):\n", merged_tree)
