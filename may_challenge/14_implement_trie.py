class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node(letter)
            node = node.children[letter]
        
        node.children[None] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        
        for letter in word:
            if letter not in node.children:
                return False

            node = node.children[letter]
        
        return None in node.children

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        
        for letter in prefix:
            if letter not in node.children:
                return False

            node = node.children[letter]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
