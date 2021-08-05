'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''

#method 1. DLL + dict. 
class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.dummyHead = DLLNode('*','#')
        self.dummyTail = DLLNode('*','#')
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            val = self.d[key].val
            self.put(key, val)
            return val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if len(self.d) == self.capacity:
            if key not in self.d:
                self.d.pop(self.dummyHead.next.key)
                self.remove(self.dummyHead.next)
            else:
                self.remove(self.d[key])
        elif key in self.d:
            self.remove(self.d[key])
        self.add(key, value)
                  
    def add(self, key, value):
            curr = DLLNode(key, value)
            prev = self.dummyTail.prev
            prev.next = curr
            curr.prev = prev
            curr.next = self.dummyTail
            self.dummyTail.prev = curr
            self.d[key] = curr
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
