class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = self.process(S)
        stack_t = self.process(T)

        return stack_t == stack_s

    def process(self, keys):
        stack = []
        for key in keys:
            if key == '#':
                if len(stack) > 0:
                    stack.pop()
                continue

            stack.append(key)

        return stack
