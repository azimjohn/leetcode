package main

import "fmt"

func main() {
	fmt.Println(isAnagram("nagaram", "anagram"))
	fmt.Println(isAnagram("rat", "car"))
}

func isAnagram(s, t string) bool {
	if len(s) != len(t) {
		return false
	}

	c1 := counter(s)
	c2 := counter(t)

	if len(c1) != len(c2) {
		return false
	}

	for k := range c1 {
		v1, v2 := c1[k], c2[k]
		if v1 != v2 {
			return false
		}
	}

	return true
}

func counter(s string) map[rune]int {
	c := make(map[rune]int)

	for _, char := range s {
		c[char]++
	}

	return c
}
