func setZeroes(matrix [][]int)  {
    zeroCols := make(map[int]bool)
    zeroRows := make(map[int]bool)
	numCols, numRows := len(matrix), len(matrix[0])

	for i, col := range matrix {
		for j, elem := range col {
			if elem == 0 {
				zeroCols[i] = true
				zeroRows[j] = true
			}
		}
	}

	for col, _ := range zeroCols {
		for row:=0; row < numRows; row++ {
			matrix[col][row] = 0
		}
	}

	for col := 0; col < numCols; col++ {
		for row, _ := range zeroRows {
			matrix[col][row] = 0
		}
	}
}