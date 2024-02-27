from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

Tree = LinkedBinaryTree

def build_complete_binary_tree(level):
    root = Tree.Node(0)
    q = ArrayQueue()
    q.enqueue(root)
    counter = 1
    for i in range(level):
        length = len(q)
        for j in range(length):
            node = q.dequeue()
            node.left = Tree.Node(counter)
            node.right = Tree.Node(counter + 1)
            q.enqueue(node.left)
            q.enqueue(node.right)
            counter += 2
            
    return Tree(root)

#building two complete tree
complete_tree1 = build_complete_binary_tree(2)
complete_tree2 = build_complete_binary_tree(3)


#building a full tree
root_full = Tree.Node(1, Tree.Node(2, Tree.Node(4, Tree.Node(7), 
                                              Tree.Node(6, Tree.Node(4),
                                                           Tree.Node(1))),
                                 Tree.Node(5, Tree.Node(10), 
                                              Tree.Node(10))), 

                    Tree.Node(5, Tree.Node(9), 
                                 Tree.Node(9, Tree.Node(19, Tree.Node(8), Tree.Node(8)),
                                              Tree.Node(13))))

full_tree = Tree(root_full)



#EXAMPLE TREE

'''
Tree.Node(data, left = None, right = None)

root -> left
     -> right
'''

#building the tree for better visualization
root = Tree.Node(1, Tree.Node(2, Tree.Node(4, Tree.Node(7), 
                                              Tree.Node(6, Tree.Node(4),
                                                           Tree.Node(1))),
                                 Tree.Node(5, None, 
                                              Tree.Node(10))), 

                    Tree.Node(5, None, 
                                 Tree.Node(9, Tree.Node(19, Tree.Node(8)),
                                              Tree.Node(13))))

print("Example Tree:")
bin_tree = Tree(root)
print(bin_tree)












'''
LAB ANSWERS BEGIN HERE. THEY DONT NEED TO SEE HOW THE BINARY TREES ARE BUILT. 
THE TEST CASES PRINT THEM SO THEY CAN SEE WHAT EACH ONE LOOKS LIKE. 
STUDENTS WILL NOT BE GIVEN THE CODE TO PRINT TREES UNTIL FINALS WEEK. 
THEY CAN MAKE ONE THEMSELVES IF THEY'D LIKE THOUGH! :)
    
SHOW THEM THE ANSWER CODE AND EXPLAIN HOW IT WORKS. THEN EXPLAIN THE OUTPUT.
NO NEED TO EXPLAIN THE TEST CODE.
'''






#It is better for beginners to use the the case by case solution instead of the simplified solution. Just explain the beginner intuitive
#solutions. They can try to trace the simplified solutions in their own time.


#QUESTION 1
print("\n\n\nQUESTION 1: is_even_sum")
#Simple Solution (based on whether there is a node or not (None))
def bt_even_sum(root):
    if root: #if root, is the same as if root is not None, implicit conversion to True if object exists, False if None
        return bt_even_sum(root.left) + bt_even_sum(root.right) + root.data * (root.data %2 == 0)
    return 0


print("\nTesting bt_even_sum: ",bt_even_sum(bin_tree.root))


def bt_even_sum(root):
    if root is None:
        return 0

    total = 0
    if root.val % 2 == 0:
        total += root.val

    total += bt_even_sum(root.left)
    total += bt_even_sum(root.right)

    return total


#Beginner Intuitive Solution where you check by case
def bt_even_sum2(root):

    #base case where you reach a leaf node
    if root.left is None and root.right is None:
        if root.data % 2 == 0: #check if even
            return root.data   #this can be shortened to root.data * (root.data %2 == 0), the bool returns True (converted to int 1),
        return 0               #or False (converted to int 0), which you see in the simplified solution.


    if root.left is not None and root.right is not None: #contains both left and right children
        if root.data % 2 == 0:
            return root.data + bt_even_sum2(root.left) + bt_even_sum2(root.right) #check the left child
        return bt_even_sum2(root.left) + bt_even_sum2(root.right)

    
    if root.left is not None: #only contains left child
        if root.data % 2 == 0:
            return root.data + bt_even_sum2(root.left) #check the left child
        return bt_even_sum2(root.left)
    

    if root.right is not None: #only contains right child
        if root.data % 2 == 0:
            return root.data + bt_even_sum2(root.right) #check the right child
        return bt_even_sum2(root.right)



print("Testing bt_even_sum2: ", bt_even_sum2(bin_tree.root))











#QUESTION 2
print("\n\n\nQUESTION 2: Binary Tree Contains")
'''
The idea is to chain OR statements so it'll look like False or False or False ... 
for OR logic, if root.data == val, you will get one True in there, which makes the entire chain True

This is how you accumulate logic
Similar to chaining + for summation or * multiplication (factorial)
'''

def __contains__(self, item):
    return self._contains_recursive(item, self.root)

def _contains_recursive(self, item, node):
    if node is None:
        return False
    if node.data == item:
        return True
    return self._contains_recursive(item, node.left) or self._contains_recursive(item, node.right)
    

#All the answers down below use a different approach(it's a function that takes two parameters, a root node and val, and return True if val exists or False if not)


#Simple Solution (based on whether there is a node or not (None))
def bt_contains(root, val):
    if root:
        return root.data == val or bt_contains(root.right, val) or bt_contains(root.left, val)
    return False





#Beginner Intuitive Solution where you check by case (whether the node has 2 children, only left, only right, or none)
def bt_contains2(root, val):

    #base case where you reach a leaf node
    if root.left is None and root.right is None:
        return root.data == val


    if root.left is not None and root.right is not None: #contains both left and right children
        return root.data == val or bt_contains2(root.left, val) or bt_contains2(root.right, val) #could be in either one of these

    
    if root.left is not None: #only contains left child
        return root.data == val or bt_contains2(root.left, val) 
    

    if root.right is not None: #only contains right child
        return root.data == val or bt_contains2(root.right, val) 



def bt_contains3(root, val):
    
    #can do the check first instead of checking at each individual call and avoid making recursive calls once it's been found:
    if root.data == val:
        return True
    
    #base case where you reach a leaf node
    if root.left is None and root.right is None:
        return root.data == val
    
    
    if root.left is not None and root.right is not None: #contains both left and right children
        return bt_contains3(root.left, val) or bt_contains3(root.right, val) #could be in either one of these


    if root.left is not None: #only contains left child
        return bt_contains2(root.left, val)


    if root.right is not None: #only contains right child
        return bt_contains2(root.right, val)




#TEST CODE FOR QUESTION 2
failed = 0

print("\n\nTesting bt_contains: " + " ".join([str(num.data) for num in bin_tree.breadth_first()]))

for node in bin_tree.inorder():

    if (not bt_contains(bin_tree.root, node.data)):
        print("Did not detect: ", node.data)
        failed += 1
    
    if (not bt_contains2(bin_tree.root, node.data)):
        print("Did not detect: ", node.data)
        failed += 1

if (failed):
    print("Did not detect this many numbers: ", failed)
else:
    print("Passed all cases for bt_contains")










#QUESTION 3
print("\n\n\nQUESTION 3: is full")
def is_full(root):
    if root:
        has_2_children = root.left and root.right
        has_0_children = not (root.left or root.right) #not root.left and not root.right (DeMorgan's Law)
    
        #either has 2 children or 0 children
        return (has_2_children or has_0_children) and is_full(root.left) and is_full(root.right)
    
    return True


def is_full(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return is_full(root.left) and is_full(root.right)

    return False # only 1 child



print("\n\nExample Complete Tree1:\n\n", complete_tree1)
print("\ncomplete_tree1 is_full: ", is_full(complete_tree1.root))

print("\n\nExample Complete Tree2:\n\n", complete_tree2)
print("\ncomplete_tree2 is_full: ", is_full(complete_tree2.root))

print("\n\nExample non Complete Tree:\n\n", bin_tree)
print("\nExample Tree is_full: ", is_full(bin_tree.root))

print("\n\nExample Full Tree\n", full_tree)
print("\nFull Tree is_full: ", is_full(full_tree.root))




#QUESTION 4
print("\n\n\nQUESTION 4: Preorder with Stack")

class LinkedBinaryTree2(Tree): #ignore this line, just look at the method below
    
    #just look at this method below! 
    def preorder_with_stack(self):
        
        if (self.root is not None): #the binary tree is not empty
            node = self.root
            
            s = ArrayStack()
            s.push(node)
            
            while (not s.is_empty()):
                node = s.pop()
                yield node.data
                
                '''
                Preorder is D L R
                the Right Node must go in before the Left Node
                because the stack reverses the order they come out of
                
                '''
                
                if (node.right is not None):
                    s.push(node.right)
                
                if (node.left is not None):
                    s.push(node.left)
        
        
        



print("\n\nExample Complete Tree1:\n\n", complete_tree1, "\nPreorder:")
for item in complete_tree1.preorder_with_stack():
	print(item, end = ' ')
print()


print("\n\nExample Complete Tree2:\n\n", complete_tree2, "\nPreorder:")
for item in complete_tree2.preorder_with_stack():
	print(item, end = ' ')
print()


print("\n\nExample non Complete Tree:\n\n", bin_tree, "\nPreorder:")
for item in bin_tree.preorder_with_stack():
	print(item, end = ' ')
print()


print("\n\nExample Full Tree\n\n", full_tree, "\nPreorder:")
for item in full_tree.preorder_with_stack():
	print(item, end = ' ')
print()








#QUESTION 5
print("\n\n\nQUESTION 5: Merge Binary Trees")

def merge(t1, t2):
    if t1 and t2: #same as writing if t1 is not None and t2 is not None
        t3 = Tree.Node(t1.data + t2.data)
        t3.left = merge(t1.left, t2.left)
        t3.right = merge(t1.right, t2.right)
        return t3
        
    if t1: #and not t2; same as writing if t1 is not None and t2 is None
        t3 = Tree.Node(t1.data)
        t3.left = merge(t1.left, None)
        t3.right = merge(t1.right, None)
        return t3
        
    if t2: #and not t1; same as writing if t2 is not None and t1 is None
        t3 = Tree.Node(t2.data)
        t3.left = merge(None, t2.left)
        t3.right = merge(None, t2.right)
        return t3
        
    #not t1 and not t2; same as writing t1 is None and t2 is None
    return None


def merge_bt(root1, root2):
    root = merge(root1, root2) #you couldve just kept it as one function but this just shows that 
    return root                #merge will always return the root of two subtrees,
                               #with the main root being returned at the end of the recursive function
    

print("\nExample Tree 1:\n", bin_tree)
print("\nExample Tree 2:\n", complete_tree1)
merged_tree = LinkedBinaryTree(merge_bt(bin_tree.root, complete_tree1.root))
print("\nMerged Tree:\n", merged_tree)
