package main

import "fmt"

func main() {
	fmt.Println(romanToInt("III")) // expected 3
}

func romanToInt(s string) int {
	romanMap := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	total, prev := 0, 0

	for _, c := range s {
		current := romanMap[c]

		if current < prev {
			total -= prev
		} else {
			total += prev
		}
		prev = current
	}

	total += prev

	return total
}
