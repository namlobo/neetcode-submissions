class Node:
    def __init__(self,key = 0, val=0):#doubly linked list
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}#stores key value paid
        #left = LRU, right = MRU
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right, self.left 
    #helper functions remove and insert
    def remove(self,node):
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev = nxt,prev

    def insert(self,node):#insert at right
        prev,nxt = self.right.prev,self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            #todo update most recnet
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            #remove from list and delete LRU hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    #have a hashmap to store the key value , the value should be a pointer to the actual node
    #a doubly linked list between the nodes
    #most recently and least recently used pointer
        
