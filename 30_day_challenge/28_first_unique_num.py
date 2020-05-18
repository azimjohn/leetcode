class FirstUnique:
    def __init__(self, nums: List[int]):
        self.counter = collections.Counter(nums)
        self.unique = {n: True for n in self.counter if self.counter[n] == 1}

    def showFirstUnique(self) -> int:
        try:
            return next(iter(self.unique))
        except StopIteration:
            return -1

    def add(self, value: int) -> None:
        if self.counter[value] == 0:
            self.unique[value] = True

        if self.counter[value] == 1:
            del self.unique[value]

        self.counter[value] += 1
