class FirstUnique:
    def __init__(self, nums: List[int]):
        self.counter = collections.Counter(nums)
        self.queue = collections.deque(nums)

    def showFirstUnique(self) -> int:
        while self.queue and self.counter[self.queue[0]] != 1:
            self.queue.popleft()
        
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.counter[value] += 1
