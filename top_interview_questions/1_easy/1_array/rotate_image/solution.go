package main

import "fmt"

func main() {
	image := [][]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
		{13, 14, 15, 16},
	}
	rotate(image)
	fmt.Println(image)
}

func rotate(matrix [][]int) {
	size := len(matrix)
	matrixCopy := make([][]int, size)
	copy2d(matrixCopy, matrix)

	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			matrix[j][size-i-1] = matrixCopy[i][j]
		}
	}
}

func copy2d(dst, src [][]int) {
	for i := range src {
		dst[i] = make([]int, len(src[i]))
		copy(dst[i], src[i])
	}
}
