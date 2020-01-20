package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(longestCommonPrefix([]string{
		"a",
	}))
}

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	if len(strs[0]) == 0 {
		return ""
	}

	minStringLength := getMinStrLength(strs)
	lastPrefixIndex := getLastPrefixIndex(minStringLength, strs)

	return strs[0][:lastPrefixIndex]
}

func getLastPrefixIndex(minStringLength int, strs []string) int {
	for i := 0; i < minStringLength; i++ {
		char := strs[0][i]
		for _, str := range strs {
			if str[i] != char {
				return i
			}
		}
	}
	return minStringLength
}

func getMinStrLength(strs []string) int {
	minStringLength := math.MaxInt32
	for _, str := range strs {
		length := len(str)
		if length < minStringLength {
			minStringLength = length
		}
	}
	return minStringLength
}
