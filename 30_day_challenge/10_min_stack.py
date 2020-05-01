class Node:
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, value: int) -> None:
        min_value = value
        if len(self.stack) > 0:
            prev_min_value = self.stack[-1].min_value
            min_value = min(prev_min_value, min_value)
        
        node = Node(value, min_value)
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].min_value
