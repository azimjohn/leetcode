package main

import "fmt"

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb")) // expected 3
	fmt.Println(lengthOfLongestSubstring("bbbbb"))    // expected 1
	fmt.Println(lengthOfLongestSubstring("pwwkew"))   // expected 3
}

func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}

	length := len(s)
	longest := 1
	hashMap := make(map[uint8]int)
	i, j := 0, 0

	for j < length {
		char := s[j]
		if _, ok := hashMap[char]; ok {
			i = max(i, hashMap[char])
		}

		longest = max(longest, j-i+1)
		hashMap[char] = j + 1
		j += 1
	}

	return longest
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
