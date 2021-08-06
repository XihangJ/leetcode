'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''

class RandomizedSet:
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.d[val] = len(self.d)
            self.array.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d: return False
        else:
            index = self.d[val]
            tail = self.array[-1]
            self.d[tail] = index
            self.array[index], self.array[-1] = self.array[-1], self.array[index]
            self.d.pop(val)
            self.array.pop()
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randrange(0, len(self.array), 1)
        res = self.array[index]
        return res
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
