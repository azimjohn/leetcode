class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        
        increasing = True
        
        for i in range(1, n-1):
            if increasing and A[i-1] < A[i] < A[i+1]:
                continue
            
            if increasing and A[i-1] < A[i] > A[i+1]:
                increasing = False
                continue
            
            if not increasing and A[i-1] > A[i] > A[i+1]:
                continue
            
            return False
        
        return not increasing
