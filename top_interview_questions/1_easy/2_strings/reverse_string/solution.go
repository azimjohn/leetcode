package main

import "fmt"

func main() {
	bytes := []byte("Hello")
	reverseString(bytes)
	fmt.Println(string(bytes))
}

func reverseString(s []byte) {
	length := len(s)

	for i := 0; i < length/2; i++ {
		s[i], s[length-i-1] = s[length-i-1], s[i]
	}
}
