class Solution:
    def stringShift(self, string: str, shifts: List[List[int]]) -> str:
        shift_sum = 0
        for shift in shifts:
            if shift[0] == 0:
                shift_sum += shift[1]
            else:
                shift_sum -= shift[1]

        shift_sum = shift_sum % len(string)

        return string[shift_sum:] + string[:shift_sum] 
