from collections import deque
class MyStack:
    #method2. 1 queue
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        n = len(self.q)
        self.q.append(x)
        while n > 0:
            self.q.append(self.q.popleft())
            n -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q: return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q: return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.q: return False
        else: return True
    
    
    
    '''
    #method1. 2 queues
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1: return self.q1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1: return self.q1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.q1: return False
        else: return True
    '''
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
