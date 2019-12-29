letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = letters[digits[0]].copy()
        for d in digits[1:]:
            result = self.multiply(result, letters[d])
        
        return result

    def multiply(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        
        for l1 in list1:
            for l2 in list2:
                result.append(l1 + l2)
        
        return result
