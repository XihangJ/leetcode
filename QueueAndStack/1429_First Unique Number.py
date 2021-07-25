from collections import OrderedDict
class FirstUnique: 
    '''
    #method 2. LinkedHashSet for Queue, and HashMap of Unique-Statuses
    #constructor: O(K), add(): O(1), showFirstUnique(): O(1). S(N)
    def __init__(self, nums: List[int]):
        self.d = OrderedDict()
        self.repeated = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.d:
            return next(iter(self.d))
        return -1

    def add(self, value: int) -> None:
        if value in self.d:
            self.d.pop(value)
            self.repeated.add(value)
        elif value not in self.repeated:
            self.d[value] = True
    '''
    
    
    #method 1. Queue and HashMap of Unique-Status. 
    #constructor: O(K), add(): O(1), showFirstUnique(): O(1) (amortized). S(N)
    def __init__(self, nums: List[int]):
        self.d = {}
        self.q = deque()
        for num in nums:
            if num in self.d:
                self.d[num] = False
            else:
                self.d[num] = True
                self.q.append(num)

    def showFirstUnique(self) -> int:
        while (self.q) and (self.q[0] in self.d) and (self.d[self.q[0]] == False):
            self.q.popleft()
        if self.q: return self.q[0]
        else: return -1

    def add(self, value: int) -> None:
        if value in self.d:
            self.d[value] = False
        else:
            self.d[value] = True
            self.q.append(value)            
    

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
