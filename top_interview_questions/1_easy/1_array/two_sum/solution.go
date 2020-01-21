package main

import "fmt"

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9)) // expected []int{0, 1}
}

func twoSum(nums []int, target int) []int {
	complements := make(map[int]int)

	for i, num := range nums {
		complements[target-num] = i
	}

	for j, num := range nums {
		i, exists := complements[num]

		if !exists {
			continue
		}

		if i != j {
			return []int{i, j}
		}
	}

	return []int{-1, -1}
}
