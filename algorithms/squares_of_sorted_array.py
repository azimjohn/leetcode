def sortedSquares(A: List[int]) -> List[int]:
    index = len(A) - 1
    results = [0 for _ in A]
    negative, positive = 0, len(A) - 1
    while index >= 0:
        if abs(A[negative]) > A[positive]:
            results[index] = A[negative] ** 2
            negative += 1
        else:
            results[index] = A[positive] ** 2
            positive -= 1
        index -= 1
    return results
