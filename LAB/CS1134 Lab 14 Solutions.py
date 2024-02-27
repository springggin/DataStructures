from ChainingHashTableMap import ChainingHashTableMap
from DoublyLinkedList import DoublyLinkedList

'''
try/except is similar to if else
since the __contains__ method was not defined in lecture
you can't do if key in map ... 

therefore, we will use try/except

try: ... try to do this
except: ... if error, do this instead
'''


lst = [1, 2, 3, 4, 3, 2, 1, 4, 5, 3, 3, 4, 2, 2, 2, 4, 4, 4, 4]
def most_frequent(lst):
    fmap = ChainingHashTableMap()
    for num in lst: 
        if num not in fmap:
            fmap[num] = 0
        fmap[num] += 1
    
    max_num = None
    max_count = 0

    for key in fmap:
        if fmap[key] > max_count:
            max_num = key
            max_count = fmap[key]

    return max_num

print("\nQUESTION 1a")
print(most_frequent(lst))


def first_unique(lst):
    fmap = ChainingHashTableMap()
    for num in lst: 
        if num not in fmap:
            fmap[num] = 0
        fmap[num] += 1
    
    #to find the first unique number
    for num in lst:
        if fmap[num] == 1: #first unique number
            return num

    return None #no unique numbers

print("\nQUESTION 1b")
print(first_unique(lst))


'''
QUESTION 1c

Extra space complexity = O(n) because worst-case the list contains only one duplicate pair, while the
rest of the list is unique ex) [1, 1, 2, 3, 4, 5, 6, 7 ... ]
In this case, if the len of the list were n, we would have n-1 different keys in the list.

If the input were a string of alphabet characters, the extra space complexity is constant O(1)
because there are only a constant set of alphabet characters: 52 (26 lower and 26 upper case)
this set is finite so it ranges from 1 to 52, whereas numbers can go from 1 to "infinity"

'''








def two_sum(lst, target):
    seen = ChainingHashTableMap() #(key, val) = (num, index)

    for i in range(len(lst)):
        try:
            if seen[target-lst[i]]:
                return (seen[target - lst[i]], i)
        except:
            seen[lst[i]] = i
    
    return (None, None)

print("\nQUESTION 2")
print(two_sum([-2, 11, 15, 21, 20, 7], 22)) #(2, 5) because 15 + 7 = 22
print(two_sum([-2, 11, 15, 21, 20, 7], 26)) #(1, 2) because 11 + 15 = 26
print(two_sum([-2, 11, 15, 21, 20, 17], 22)) #(None, None)








#QUESTION 3: Play List (2 Solutions)

#Key, Val pair, key = Song name, val = ref to Node in the DLL.
#Node.data is the song name as well

'''
    pl = PlayList( ) - creates an empty PlayList object.
    pl.add_song(new_song_name) - adds the song new_song_name to the end of the songs sequence
    pl.add_song_after(song_name, new_song_name) - adds the song new_song_name to the songs sequence, right after song_name; or raise KeyError exception if song_name not in the play list
    pl.play_song(song_name) - plays the song song_name; or raise KeyError exception if song_name not in the play list
    pl.play_list( )
    '''

class PlayList: #Time = Theta(1), Theta(n), Extra Space = O(n)
    
    def __init__(self):
        self.songs = ChainingHashTableMap()
        self.songs_list = DoublyLinkedList() #maintain FIFO order with O(1) insert
    
    
    def add_song(self, new_song_name):
        self.songs_list.add_last(new_song_name)
        self.songs[new_song_name] = self.songs_list.trailer.prev #last node
    
    
    def add_song_after(self, song_name, new_song_name):
        if song_name not in self.songs:
            raise KeyError("Song:",song_name,"not found.")
        
        self.songs_list.add_after(self.songs[song_name], new_song_name) #add node after song_name node
        self.songs[new_song_name] = self.songs[song_name].next
    
    
    def play_song(self, song_name):
        if song_name not in self.songs:
            raise KeyError("Song:", song_name,"not found.")
        
        print("Playing:", song_name,"\b.") #\b is backspace, just for formatting (not required)
    
    
    def play_list(self): #Iterate through the doubly linked list
        for song in self.songs_list:
            print("Playing:", song,"\b.")


print("\nQUESTION 3")

print("\nTesting PlayList1 with HashMap and DLL")
p1 = PlayList( )
p1.add_song("Jana Gana Mana") 
p1.add_song("Kimi Ga Yo") 
p1.add_song("The Star-Spangled Banner") 
p1.add_song("March of the Volunteers") 
p1.add_song_after("The Star-Spangled Banner", "La Marcha Real")
p1.add_song_after("Kimi Ga Yo", "Aegukga") 
p1.add_song("Arise, O Compatriots")
p1.add_song("Chant de Ralliement") 
p1.add_song_after("Chant de Ralliement", "Himno Nacional Mexicano")
p1.add_song_after("Jana Gana Mana", "God Save The Queen")

p1.play_song("The Star-Spangled Banner")
p1.play_song("Jana Gana Mana")

p1.play_list( )






#Without extra space --> Key, Val pair, Key = song name, val = next song name
#Simulate a singly linked list

class PlayList2: #Time = Theta(1), Theta(n), Extra Space = O(1)
    
    def __init__(self):
        self.songs = ChainingHashTableMap()
        self.first = None #We need a beginning reference for playing the songs in FIFO
        
        self.last = None  #keep reference to last so adding to last in a singly linked list is O(1)
    #otherwise, we have to iterate over the entire singly linked list
    #since we don't need to delete, we don't worry about losing reference to last
    
    
    def add_song(self, new_song_name):
        if self.last is None: #empty singly linked list (only empty once because we don't delete songs)
            self.songs[new_song_name] = None
            self.first = new_song_name
        else:
            self.songs[self.last] = new_song_name
            self.songs[new_song_name] = None
    
        self.last = new_song_name #avoid repeated code, take this out of both if/else.

    
    def add_song_after(self, song_name, new_song_name):
        if song_name not in self.songs:
            raise KeyError("Song:", song_name,"not found.")
        
        if self.last == song_name:
            self.add_song(new_song_name) #add to end of play list
        
        else:                                                 #A = song_name, B = after song_name, C = new song_name
            self.songs[new_song_name] = self.songs[song_name] #[A] --> [B], make [C] --> [B]
            self.songs[song_name] = new_song_name             #[A] --> [C]
    #[A] --> [C] --> [B]


    def play_song(self, song_name):
        if song_name not in self.songs:
            raise KeyError("Song:", song_name,"not found.")
        
        print("Playing:", song_name,"\b.") #\b is backspace, just for formatting (not required)
    

    def play_list(self):
        curr_song = self.first
        while curr_song is not None:
            print("Playing:", curr_song,"\b.")
            curr_song = self.songs[curr_song] #remember, the val is the next "node"



print("\nTesting PlayList2 with ONLY HashMap (simulating SLL)")
p2 = PlayList( )
p2.add_song("Jana Gana Mana") 
p2.add_song("Kimi Ga Yo") 
p2.add_song("The Star-Spangled Banner") 
p2.add_song("March of the Volunteers") 
p2.add_song_after("The Star-Spangled Banner", "La Marcha Real")
p2.add_song_after("Kimi Ga Yo", "Aegukga") 
p2.add_song("Arise, O Compatriots")
p2.add_song("Chant de Ralliement") 
p2.add_song_after("Chant de Ralliement", "Himno Nacional Mexicano")
p2.add_song_after("Jana Gana Mana", "God Save The Queen")

p2.play_song("The Star-Spangled Banner")
p2.play_song("Jana Gana Mana")

p2.play_list( )

















import random
from DoublyLinkedList import DoublyLinkedList

#CHANGES ARE COMMENTED OUT SO STUDENTS CAN SEE THE DIFFERENCE

class ChainingHashTableSet:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N


    def __init__(self, N=64):
        self.N = N

        # self.table = [UnsortedArrayMap() for i in range(self.N)] 
        self.table = [DoublyLinkedList() for i in range(self.N)] 

        self.n = 0

        # self.hash_function = ChainingHashTableMap.MADHashFunction(N)
        self.hash_function = ChainingHashTableSet.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    # def __getitem__(self, key):       #DONT NEED SINCE WE DONT HAVE VALUES!
    #     i = self.hash_function(key)
    #     curr_bucket = self.table[i]
    #     return curr_bucket[key]


    # def __setitem__(self, key, value):
    def add(self, key):
        if key not in self: #trying to add an existing key does not change the set
            i = self.hash_function(key)
            curr_bucket = self.table[i]
            old_size = len(curr_bucket)

            # curr_bucket[key] = value
            curr_bucket.add_last(key)   

            new_size = len(curr_bucket)
            if (new_size > old_size):
                self.n += 1
            if (self.n > self.N):
                self.rehash(2 * self.N)


    # def __delitem__(self, key):
    def remove(self, key):
        if key not in self:
            raise KeyError("Key: "+str(key)+" does not exist in set")


        i = self.hash_function(key)
        curr_bucket = self.table[i]

        # del curr_bucket[key]
        curr_node = curr_bucket.header
        while curr_node is not curr_bucket.trailer:
            if curr_node.data == key:
                curr_bucket.delete_node(curr_node)
                break
            curr_node = curr_node.next

        self.n -= 1
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    # def __contains__(self, key)
    #     try:
    #         val = self[key] #we can't do this because we don't have a __getitem__ 
    #         return True     #we do not need __getitem__ since there is no key value pair, just keys
    #     except KeyError:
    #         return False

    def __contains__(self, key):    #therefore, manually search the bucket
        i = self.hash_function(key) 
        curr_bucket = self.table[i]

        for data in curr_bucket: #would do for key in curr_bucket but key is the parameter name too ... :(
            if data == key:         
                return True
        return False
        

    def __iter__(self):
        for curr_bucket in self.table:
            for key in curr_bucket:
                yield key
            

    def rehash(self, new_size):
        # old = [(key, self[key]) for key in self]
        old = [key for key in self]

        self.__init__(new_size)

        # for (key, val) in old:
        #     self[key] = val
        for key in old:
            self.add(key)


def print_hash_set(hset):
    # print("{", end= "")
    # for i in range(hset.N):
    #     curr_bucket = hset.table[i]
    #     for key in curr_bucket:
    #         print(key, end = ", ")

    # print("}")

    #or you can just do this one liner
    print("{" + ", ".join([" ".join([str(key) for key in hset.table[i]]) for i in range(hset.N) if hset.table[i]]) + "}")



#TEST CODE
hash_set = ChainingHashTableSet()
hash_set.add(5)
hash_set.add(2)
hash_set.add(2)
hash_set.add(11)
hash_set.add(2)
hash_set.add(4)
hash_set.add(9)
hash_set.add(2)

print("\nQUESTION 4")
print_hash_set(hash_set)
print(5 in hash_set)
hash_set.remove(5)
print_hash_set(hash_set)
print(5 in hash_set)


hash_set.add(2)
hash_set.add(7)
print_hash_set(hash_set)
