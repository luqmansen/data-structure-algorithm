import math

class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.min) > 0:
            if val <= self.min[-1]:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
        else:
            self.min.append(val)
        
    def pop(self) -> None:
        self.min.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()