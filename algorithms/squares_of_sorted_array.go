func sortedSquares(A []int) []int {
	results := make([]int, len(A))
	index := len(A) - 1
	negative, positive := 0, len(A) - 1

	for index >= 0 {
		if square(A[negative]) > square(A[positive]) {
			results[index] = square(A[negative])
			negative += 1
		} else {
			results[index] = square(A[positive])
			positive -= 1
		}

		index -= 1
	}

	return results
}

func square(n int) int {
	return n * n
}
