import random


class Solution:

    def __init__(self, w: List[int]):
        self.indexes = list(range(len(w)))
        self.weights = w

    def pickIndex(self) -> int:
        return random.choices(self.indexes, self.weights)[0]
