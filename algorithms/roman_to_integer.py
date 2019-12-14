roman_dict = {
    'I': 1,
    'V':5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        prev = 0
        total = 0
        for char in s:
            current = roman_dict[char]
            
            if prev < current:
                total -= prev
            else:
                total += prev

            prev = current
        
        total += prev
        
        return total
