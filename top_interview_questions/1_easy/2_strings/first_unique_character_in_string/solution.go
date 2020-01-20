package main

import "fmt"

func main() {
	fmt.Println(firstUniqChar("Azimjon")) // expected 0
}

func firstUniqChar(s string) int {
	hashMap := make(map[rune]int)

	for _, char := range s {
		hashMap[char] += 1
	}

	for i, char := range s {
		count, _ := hashMap[char]
		if count == 1 {
			return i
		}
	}

	return -1
}
