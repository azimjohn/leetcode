package main

type Node struct {
	val      int
	minSoFar int
}

type MinStack struct {
	stack []Node
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{stack: []Node{}}
}

func (s *MinStack) Push(x int) {
	length := len(s.stack)
	min := x
	if length > 0 {
		minSoFar := s.stack[length-1].minSoFar
		if min > minSoFar {
			min = minSoFar
		}
	}

	s.stack = append(s.stack, Node{
		val:      x,
		minSoFar: min,
	})
}

func (s *MinStack) Pop() {
	length := len(s.stack)
	s.stack = s.stack[:length-1]
}

func (s *MinStack) Top() int {
	length := len(s.stack)
	return s.stack[length-1].val
}

func (s *MinStack) GetMin() int {
	length := len(s.stack)
	return s.stack[length-1].minSoFar
}
