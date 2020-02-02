package main

import "fmt"

func main() {
	fmt.Println(longestPalindrome("babad")) // bab
	fmt.Println(longestPalindrome("cbbd"))  // bb
}

func longestPalindrome(s string) string {
	s = duplicateChars(s)
	longest := ""
	current := ""
	length := len(s)

	for n := 0; n < length; n++ {
		i := 0
		for n-i >= 0 && n+i < length-1 {
			fmt.Println(n, i)
			if s[n-i] != s[n+i+1] {
				break
			}
			i++
		}

		current = s[n-i+1 : n+i+1]
		if len(current) > len(longest) {
			longest = current
		}
	}

	return removeDuplicates(longest)
}

func duplicateChars(s string) string {
	r := ""

	for _, char := range s {
		r += string(char)
		r += string(char)
	}

	return r
}

func removeDuplicates(s string) string {
	r := ""
	for i, char := range s {
		if i%2 == 0 {
			r += string(char)
		}
	}

	return r
}
