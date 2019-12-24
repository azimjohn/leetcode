class Solution:
    def __init__(self):
        self.letters = {}
        self.letters_count = 26
        self.fill_letters()
    
    def fill_letters(self):
        for i in range(self.letters_count):
            self.letters[chr(65+i)] = i + 1

    def titleToNumber(self, s: str) -> int:
        result = 0
    
        for index, char in enumerate(reversed(s)):
            result += (self.letters_count ** index) * self.letters[char]

        return result
