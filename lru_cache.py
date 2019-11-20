# https://leetcode.com/problems/lru-cache/
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value = self.cache[key]
        del self.cache[key]
        self.cache[key] = value

        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            least_used = next(iter(self.cache.keys()))
            
            del self.cache[least_used]

        if key in self.cache:
            del self.cache[key]
    
        self.cache[key] = value
