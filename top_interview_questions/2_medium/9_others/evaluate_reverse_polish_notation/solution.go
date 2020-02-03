package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(evalRPN([]string{"4", "13", "5", "/", "+"}))
}

type stack []int

func (s stack) Push(v int) stack {
	return append(s, v)
}

func (s stack) Pop() (stack, int) {
	l := len(s)
	return s[:l-1], s[l-1]
}

func evalRPN(tokens []string) int {
	var s stack
	var operator string
	var r, operandOne, operandTwo int

	operators := map[string]bool{
		"+": true,
		"-": true,
		"*": true,
		"/": true,
	}

	for _, token := range tokens {
		if !operators[token] {
			n, _ := strconv.Atoi(token)
			s = s.Push(n)
			continue
		}

		operator = token
		s, operandTwo = s.Pop()
		s, operandOne = s.Pop()

		switch operator {
		case "+":
			r = operandOne + operandTwo
		case "-":
			r = operandOne - operandTwo
		case "*":
			r = operandOne * operandTwo
		case "/":
			r = operandOne / operandTwo
		}
		fmt.Printf("%d%s%d=%d\n", operandOne, operator, operandTwo, r)
		s = s.Push(r)
	}

	if len(s) > 0 {
		s, r = s.Pop()
	}

	return r
}
