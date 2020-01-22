package main

import "fmt"

func main() {
	fmt.Println(isValid("[(){}]")) // expected true
	fmt.Println(isValid("[(){])")) // expected false
}

type stack []rune

func (s stack) Push(v rune) stack {
	return append(s, v)
}

func (s stack) Pop() (stack, rune) {
	l := len(s)
	return s[:l-1], s[l-1]
}

func isValid(s string) bool {
	var stack stack
	var close_ rune

	braces := map[rune]rune{
		'}': '{',
		']': '[',
		')': '(',
	}

	for _, c := range s {
		open, exists := braces[c]
		if exists {
			if len(stack) > 0 {
				stack, close_ = stack.Pop()
				if open != close_ {
					return false
				}
			} else {
				return false
			}
		} else {
			stack = stack.Push(c)
		}
	}

	return len(stack) == 0
}
