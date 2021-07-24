from collections import deque
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.q1 = deque(v1)
        self.q2 = deque(v2)
        self.flag = 1

    def next(self) -> int:
        if self.flag == 1:
            if self.q1:
                res = self.q1.popleft()
                if self.q2: self.flag = 2
                return res
            elif self.q2: 
                res = self.q2.popleft()
                self.flag = 2
                return res
            else: return False
        elif self.flag == 2:
            if self.q2:
                res = self.q2.popleft()
                if self.q1: self.flag = 1
                return res
            elif self.q1:
                res = self.q1.popleft()
                self.flag = 1
                return res
            else: return False
        
            
    def hasNext(self) -> bool:
        if not self.q1 and not self.q2: return False
        else: return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
