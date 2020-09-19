class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = "123456789"
        low_size = len(str(low))
        high_size = len(str(high))
        
        for i in range(low_size, high_size+1):
            for j in range(i, 10):
                num = int(digits[j-i:j])
                if low <= num <= high:
                    result.append(num)

        return result
