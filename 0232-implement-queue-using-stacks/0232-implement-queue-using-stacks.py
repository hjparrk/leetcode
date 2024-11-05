class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = []
        for _ in range(len(self.stack) - 1):
            temp.append(self.stack.pop())
        popped = self.stack.pop()
        for _ in range(len(temp)):
            self.stack.append(temp.pop())
        return popped

    def peek(self) -> int:
        return self.stack[0]
        
    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()