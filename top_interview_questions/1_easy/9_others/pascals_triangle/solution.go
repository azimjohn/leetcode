package main

import "fmt"

func main() {
	triangle := generate(10)
	for _, row := range triangle {
		fmt.Println(row)
	}
}

func generate(numRows int) [][]int {
	rows := make([][]int, numRows)

	for i := 0; i < numRows; i++ {
		for j := 0; j < i+1; j++ {
			rows[i] = append(rows[i], 1)
		}
	}

	for i := 1; i < numRows; i++ {
		for j := 1; j < i; j++ {
			rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
		}
	}

	return rows
}
