import BinarySearchTreeMap

#QUESTION 1
def min_max_BST(bst):
   minimum = bst.root
   maximum = bst.root

   while minimum.left is not None: #left most is minimum
       minimum = minimum.left

   while maximum.right is not None: #right most is maximum
       maximum = maximum.right

   return (minimum.item.key, maximum.item.key)


#QUESTION 2

#note that youre basically going in a zig zag path, deciding whether to go left or right each time 
def gtl_n(root, n):
    curr = root  # creates a pointer to the root node
    gtln = -1 # if the tree contains no number gtln N return -1

    while curr is not None: #while we have numbers to check
        if n == curr.item.key:
            return curr.item.key #N is the greatest number gtln N

        if n > curr.item.key:
            gtln = curr.item.key
            curr = curr.right  # looking right for a potentially larger gtln

        elif n < curr.item.key:
            curr = curr.left # looking left for a smaller value gtln than n

    return gtln


#QUESTION 3

#We know that inorder of a BST is a sorted, so we can just compare the inorder results
def compare_BST(bst1, bst2):
    if len(bst1) != len(bst2):
        return False

    inorder1 = [key for key,val in bst1]
    inorder2 = [key for key,val in bst2]

    for i in range(min(len(inorder1), len(inorder2))): 
        if inorder1[i] != inorder2[i]:
            return False
    return True




#QUESTION 4
def is_bst(root):
    return is_bst_helper(root)[2]
    
def is_bst_helper(root):
    if not root:
        return None, None, True
        
    # check subtrees
    lmin, lmax, lbst = is_bst_helper(root.left)
    rmin, rmax, rbst = is_bst_helper(root.right)
    
    # if either subtree is not a bst
    if not (lbst and rbst):
        return None, None, False
        
    # if there is left, check that the max is less than current
    if lmax and lmax >= root.data:
        return None, None, False
        
    # if there is right, check that the min is greater than current
    if rmin and rmin <= root.data:
        return None, None, False
        
    # get new min and max
    dmin = lmin or root.data
    dmax = rmax or root.data
    return (dmin, dmax, True)




#another solution that may be easier to understand?

#QUESTION 4

def is_bst(root):
    if root is None: #simple case, an empy tree is still a binary search tree
        return True
    return is_bst_helper(root)[2]
    
def is_bst_helper(root):
    if root.left is None and root.right is None: #leaf node
        return (root.data, root.data, True)
        

    compare_left = True #default
    new_min = root.data #default, set as curr data
        
    if root.left is not None:
        #left subtree returns (min, max, val)
        left_tree = is_bst_helper( root.left)

        #for lett side, left subtree's min < left subtree's max < curr.data
        compare_left = compare_left and (left_tree[0] <= left_tree[1] <= root.data)

        #check immediate left, curr left val < curr.data
        compare_left = compare_left and (root.left.data < root.data)

        #compare with the bool carried over
        compare_left = compare_left and left_tree[2]

        new_min = left_tree[0] #update to be min of left subtree
            

    compare_right = True #default
    new_max = root.data  #default, set as curr data
        
    if root.right is not None:
        #right subtree returns (min, max, val)
        right_tree = is_bst_helper(root.right)

        #for right side, curr.data < right subtree's min < right subtree's max
        compare_right = compare_right and (root.data <= right_tree[0] <= right_tree[1])

        #check immediate right, curr right val > curr.data
        compare_right = compare_right and (root.right.data > root.data)

        #compare with the bool carried over
        compare_right = compare_right and right_tree[2]

        new_max = right_tree[1] #update to be max of right subtree
    
    return (new_min, new_max, compare_left and compare_right)


#BONUS
'''
in a bst, the lca is the node that is in between node1 and node2 like so 
    node1.data <= lca.data <= node2.data

starting from the root, you traverse either left or right
if both nodes are strictly less than the root:
    go left because there is definitely a lower common ancestor below root on the left side
if both nodes are strictly greater than the root:
    go right because there is definitely a lower common ancestor below root on the right side

'''
def lca_BST(root, node1, node2):
    curr = root
    while curr is not None:
        if curr.data < node1.data and curr.data < node2.data:
            curr = curr.right
        elif curr.data > node1.data and curr.data > node2.data:
            curr = curr.left
        else: #p.val <= curr.val <= q.val or q.val <= curr.val <= p.val:
            return curr
    return root

'''
in a regular binary tree, there is no relationship to determine where the lca could be.
Therefore you must use two lists and find the path of nodes that lead to node1 and node2
Then, pop from the longer list until both lists have same length (same height)
from there, pop from both the lists if lst1[-1] != lst2[-1]
'''
