package main

import (
	"fmt"
	"strings"
)

const (
	Uppercase    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	Lowercase    = "abcdefghijklmnopqrstuvwxyz"
	Alphabetic   = Uppercase + Lowercase
	Numeric      = "0123456789"
	Alphanumeric = Alphabetic + Numeric
)

func main() {
	fmt.Println(isPalindrome("flool"))
}

func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	clean := ""

	// better: regex, _ := regexp.Compile("[A-Z0-9]+")
	for _, c := range s {
		if strings.Contains(Alphanumeric, string(c)) {
			clean += string(c)
		}
	}

	length := len(clean)

	for i := 0; i < length/2; i++ {
		if clean[i] != clean[length-i-1] {
			return false
		}
	}

	return true
}
