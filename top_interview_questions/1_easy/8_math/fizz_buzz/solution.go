package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(fizzBuzz(20))
}

func fizzBuzz(n int) []string {
	result := []string{}

	for i := 1; i <= n; i++ {
		if i%15 == 0 {
			result = append(result, "FizBuzz")
		} else if i%5 == 0 {
			result = append(result, "Buzz")
		} else if i%3 == 0 {
			result = append(result, "Fiz")
		} else {
			result = append(result, strconv.Itoa(i))
		}
	}

	return result
}
