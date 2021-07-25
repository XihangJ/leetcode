class MyQueue:
    #method 2. 2 stacks. push(): O(1), pop(): O(1) (amortized). S(N)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        res = self.peek()
        self.stack2.pop()
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2: return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2 
    
    
    
    
    '''
    #method 1. 2 stacks. push(): O(n), pop(): O(1). S(N)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack1: self.stack1.append(x)
        else:
            while self.stack1:
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
            self.stack2.append(x)
            while self.stack2:
                tmp = self.stack2.pop()
                self.stack1.append(tmp)
        
        print(self.stack1)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack1:
            tmp = self.stack1.pop()
            return tmp
        else:
            raise IndexError('Can not pop element from an empty queue')

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack1:
            return self.stack1[-1]
        else:
            raise IndexError('Can not peek element from an empty queue')

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack1: return False
        else: return True
    '''

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
