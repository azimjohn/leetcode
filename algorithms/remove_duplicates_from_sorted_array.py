class Solution:
    def removeDuplicates(self, numbers: List[int]) -> int:
        previous = float('-inf')
        index = len(numbers) - 1
        
        for number in reversed(numbers):
            if number == previous:
                del numbers[index]
            previous = number
            index -= 1
    
