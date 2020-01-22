package main

import "fmt"

func main() {
	fmt.Println(containsDuplicate([]byte{'1', '2', '2', '.'}))      // expected true
	fmt.Println(containsDuplicate([]byte{'1', '2', '3', '.', '.'})) // expected false
}

func isValidSudoku(board [][]byte) bool {
	if !validRows(board) {
		return false
	}

	if !validColumns(board) {
		return false
	}

	if !validGrids(board) {
		return false
	}

	return true
}

func validRows(board [][]byte) bool {
	for _, row := range board {
		if containsDuplicate(row) {
			return false
		}
	}

	return true
}

func validColumns(board [][]byte) bool {
	var column []byte
	for i := 0; i < 9; i++ {
		column = []byte{}
		for j := 0; j < 9; j++ {
			column = append(column, board[j][i])
		}

		if containsDuplicate(column) {
			return false
		}
	}

	return true
}

func validGrids(board [][]byte) bool {
	var grid []byte
	for i := 0; i < 9; i += 3 {
		for j := 0; j < 9; j += 3 {
			grid = []byte{
				board[0+i][0+j], board[0+i][1+j], board[0+i][2+j],
				board[1+i][0+j], board[1+i][1+j], board[1+i][2+j],
				board[2+i][0+j], board[2+i][1+j], board[2+i][2+j],
			}
			if containsDuplicate(grid) {
				return false
			}
		}
	}

	return true
}

func containsDuplicate(chars []byte) bool {
	hashMap := make(map[byte]bool)

	for _, c := range chars {
		if c == '.' {
			continue
		}
		_, exists := hashMap[c]
		if exists {
			return true
		}

		hashMap[c] = true
	}

	return false
}
