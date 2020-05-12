class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min)==0 or x<=self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        x=self.stack.pop()
        if x == self.min[-1]:
            self.min.pop()
        return x

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
# Your MinStack object will be instantiated and called as such:
x=5
obj = MinStack()
obj.push(x)
obj.push(x-1)
obj.push(x+1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)

