# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def __init__(self):
        self.letters = {}
        self.letters_count = 26
        self.fill_letters()

    def fill_letters(self):
        self.letters[0] = 'Z'
        for i in range(self.letters_count):
            self.letters[i + 1] = chr(65+i)

    def convertToTitle(self, n: int) -> str:
        result = []

        while n > self.letters_count:
            rem = n % self.letters_count
            n = n // self.letters_count
            result.append(self.letters[rem])
            if rem == 0:
                n -= 1
        
        result.append(self.letters[n])
        
        return "".join(reversed(result))
