class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = dict()
        self.list = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            
            return True
        
        return False
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            index = self.dict.pop(val)
            self.list[index] = self.list[-1]
            
            last_val = self.list.pop()
            if last_val != val:
                self.dict[last_val] = index
            
            return True

        return False
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)
