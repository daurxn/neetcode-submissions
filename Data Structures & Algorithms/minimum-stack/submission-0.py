class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        i = len(self.stack) - 1
        value = self.stack[i]
        while i >= 0:
            if self.stack[i] < value:
                value = self.stack[i]
            i -= 1
        return value
