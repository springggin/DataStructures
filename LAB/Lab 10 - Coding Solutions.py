from DoublyLinkedList import DoublyLinkedList

# Question 1
class LinkedStack:

    def __init__(self):
        self.data = DoublyLinkedList()
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        self.data.add_last(e)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty!")
        return self.data.delete_last()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is Empty!")
        return self.data.trailer.prev.data
        
'''
s = LinkedStack()
s.push(5)
s.pop()
s.push(10)
s.push(12)
s.push(6)
s.push(6)

print(s.data)
print(s.top())
'''

#Question 2

class DLL(DoublyLinkedList): #ignore this part

    #just look at the method below, here 
    #add this part to the DoublyLinkedList implementation from class

    def __getitem__(self, ind):
    
        if 0 <= ind <= len(self)//2 : #if ind is in first half, start from header

            start = self.header.next              #first node (index 0)
            for i in range(ind):
                start = start.next                #bump the pointer to next

            return start.data
        
        elif len(self)//2 < ind < len(self): # if ind in second half, start from trailer

            start = self.trailer.prev             #last node (index  = len(lst) - 1)
            for i in range(len(self)-1, ind, -1): #iterate backwards
                start = start.prev                #bump the pointer backwards

            return start.data

        else: #out of bounds
            raise IndexError("Index out of range!")



'''
DoublyLinkedList = DLL

dll = DoublyLinkedList()
dll.add_last(5)
dll.add_last(2)
dll.add_first(6)
dll.add_last(8)
dll.add_first(10)
dll.add_first(4)
dll.add_last(1)
print(dll)

for i in range(len(dll)):
    print(dll[i])






print("compiled successfully")
'''

#Question 3

class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = None #starts off None for empty DLL

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    

    def push(self, e):
        self.data.add_last(e) #add to top of stack

        if len(self) == 1: #only 1 element (was empty before)
            self.mid = self.data.trailer.prev #mid is last node 
        
        elif len(self) % 2 != 0: #if len is odd, bump pointer up
            self.mid = self.mid.next


    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        val = self.data.delete_last()

        if self.is_empty():
            self.mid = None

        elif len(self) % 2 == 0: #if len is even, bump pointer down
            self.mid = self.mid.prev
        
        return val
    

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.data.trailer.prev.data
    

    def mid_push(self, e):
        self.data.add_after(self.mid, e) #add to top of stack

        if len(self) == 1: #only 1 element (was empty before)
            self.mid = self.data.trailer.prev #mid is last node 
        
        elif len(self) % 2 != 0: #if len is odd, bump pointer up
            self.mid = self.mid.next


    def get_mid(self): #optional
        return self.mid.data

'''
ms = MidStack()
print("Here")
ms.push(5)
print(ms.data, ms.get_mid())
ms.push(3)
print(ms.data, ms.get_mid())
ms.push(2)
print(ms.data, ms.get_mid())
ms.push(4)
print(ms.data, ms.get_mid())
ms.push(1)
print(ms.data, ms.get_mid())
ms.mid_push(8)
print(ms.data, ms.get_mid())
ms.mid_push(10)
print(ms.data, ms.get_mid())
ms.pop()
print(ms.data, ms.get_mid())
ms.pop()
print(ms.data, ms.get_mid())
'''

#Question 4

# SOLUTION A
def reverse_list_change_elements_order(lnk_lst):
    """Reverse the given doubly linked list by swapping node values."""
    # Get two cursors, one at the head and one at the tail
    head_cursor = lnk_lst.header.next
    tail_cursor = lnk_lst.trailer.prev

    # Keep swapping the data in them until they meet
    while head_cursor != tail_cursor:
        head_cursor.data, tail_cursor.data = tail_cursor.data, head_cursor.data # swap data
        head_cursor = head_cursor.next # move head cursor forward
        if head_cursor == tail_cursor: # edge case: for even numbered lists, need to exit here!
            break
        tail_cursor = tail_cursor.prev # move tail cursor backward

# SOLUTION B
def reverse_dll_by_node(dll):
    """Reverse the given doubly linked list by swapping node next and prev pointers.

    Pretty tricky problem! Easy to mess up different edge cases (empty list, list with one node, etc.)
    Highly recommend drawing out a picture of a doubly linked list and walking through the code
    """
    # if DLL is empty, do nothing
    if dll.is_empty():
        return

    # for all nodes, swap prev and next pointers
    current = dll.header.next
    while current is not dll.trailer:
        current.next, current.prev = current.prev, current.next
        current = current.prev

    # swap header and trailer pointers
    dll.header.next, dll.trailer.prev = dll.trailer.prev, dll.header.next

    # update prev pointer for first node
    dll.header.next.prev  = dll.header
    # update next pointer for last node
    dll.trailer.prev.next = dll.trailer

def reverse_dll_by_node_2(dll):
    """Alternative solution by swapping header and trailer at the end."""
    # for every node, including header and trailer, swap their next and prev pointers
    current = dll.header
    while current is not None:
        current.next, current.prev = current.prev, current.next
        current = current.prev

    # swap which nodes header and trailer point to
    dll.header, dll.trailer = dll.trailer, dll.header

# Question 5
class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next


        def disconnect(self):
            self.data = None
            self.next = None


    def __init__(self):
        self.header = SinglyLinkedList.Node()
        self.size = 0
        
        self.last = self.header #reference to last node, starts off as header

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val): #[a] -> [b], [a] is node, [b] is node.next
        new_node = SinglyLinkedList.Node(val)   #[c] create new node
        new_node.next = node.next #[c] -> [b]
        node.next = new_node #[a] -> [c]
        self.size += 1
        return new_node #[a] -> [c] -> [b], return [c]

    def add_first(self, val):
        node = self.add_after(self.header, val)
        if len(self) == 1: #set last node to this node if its the only node in the SLL
            self.last = node
        return node
        

    def add_last(self, val):
        self.last = self.add_after(self.last, val)
        return self.last
        

    def add_before(self, node, val):
        curr = self.header
        while curr.next is not node: #since node has no prev, we need to find the node before the input node
            curr = curr.next
        
        #ex) [a] -> [b], [b] is input node, curr = [a]
        new_node = SinglyLinkedList.Node(val) #create new node [c]
        curr.next = new_node #node before input node now references new node for next
                             #[a] -> [c], [b]
        new_node.next = node #new node now references the input node for next
                             #[a] -> [c] -> [b]
        
        self.size += 1
        return new_node
    
    
    def delete_node(self, node):
        curr = self.header
        while curr.next is not node: #since node has no prev, we need to find the node before the input node
            curr = curr.next
            
        #[a] -> [c] -> [b], input node = [c], curr = [a]
        curr.next = node.next #[a] -> [b]
        self.size -= 1
        
        val = node.data #save the data
        node.disconnect() #delete the data and next pointers from node
        return val #return the data


    def delete_first(self): #doesn't change
        if(self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.header.next)
 
    
    def delete_last(self):
        if(self.is_empty() == True):
            raise Exception("List is empty")
            
        #update self.last to the one before it.
        curr = self.header
        while curr.next is not self.last:
            curr = curr.next
            
        val = self.delete_node(self.last) #delete last node referenced by self.last
        self.last = curr #update self.last to the node before the original last node
        return val
        

    def __iter__(self):
        cursor = self.header.next
        while(cursor is not None): #changed cursor is not self.trailer to cursor is not None
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self]) + "]" #changed the <-> to  ->
