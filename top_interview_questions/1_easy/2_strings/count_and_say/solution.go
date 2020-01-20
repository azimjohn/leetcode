package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println("result", countAndSay("11"))
	fmt.Println("result", countAndSay("21"))
}

func countAndSay(num string) string {
	say := ""
	count := 1
	prev := int32(num[0])

	for _, digit := range num[1:] {
		if digit == prev {
			count += 1
			continue
		}
		say += strconv.Itoa(count) + string(prev)
		prev = digit
		count = 1
	}

	return say + strconv.Itoa(count) + string(prev)
}
