package main

import "fmt"

func main() {
	fmt.Println(strStr("Don't Panic", "Pan"))
	fmt.Println(strStr("Facebook", "book"))
}

func strStr(haystack string, needle string) int {
	needleLength := len(needle)

	for i := 0; i <= len(haystack)-needleLength; i++ {
		if haystack[i:needleLength+i] == needle {
			return i
		}
	}

	return -1
}
