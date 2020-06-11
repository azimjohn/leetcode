
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        result = []
        i, j = 0, 0

        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0])
            if A[i][1] < B[j][1]:
                if start <= A[i][1]:
                    result.append([start, A[i][1]])
                i += 1
            elif A[i][1] > B[j][1]:
                if start <= B[j][1]:
                    result.append([start, B[j][1]])
                j += 1
            else:
                result.append([start, A[i][1]])
                i += 1
                j += 1

        return result
