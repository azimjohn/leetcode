class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.children
        
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]

        current['*'] = None

    def search(self, word: str, parent=None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        parent = self.children if parent is None else parent
        if not parent:
            return False

        if not word:
            return '*' in parent
        
        char = word[0]
        if char == '.':
            for child in parent:
                if child == '*':
                    continue

                if self.search(word[1:], parent[child]):
                    return True
            return False

        if char not in parent:
            return False

        return self.search(word[1:], parent[char])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
