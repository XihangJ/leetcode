'''
Implement the RandomizedCollection class:

RandomizedCollection() Initializes the RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item was present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements (it's guaranteed that at least one element exists when this method is called). The probability of each element being returned is linearly related to the number of same values the multiset contains.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''

class RandomizedCollection:
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.d:
            self.d[val] = set([len(self.array)])
            self.array.append(val)
            return True
        else:
            self.d[val].add(len(self.array))
            self.array.append(val)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.d:
            index = self.d[val].pop()
            tail = self.array[-1]
            if index != len(self.array) - 1:
                self.d[tail].remove(len(self.array) - 1)
                self.d[tail].add(index)
            if not self.d[val]: self.d.pop(val)
            self.array[index], self.array[-1] = self.array[-1], self.array[index]
            self.array.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        index = random.randrange(0, len(self.array), 1)
        val = self.array[index]
        return val


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
