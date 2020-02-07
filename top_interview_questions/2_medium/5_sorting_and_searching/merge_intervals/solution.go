package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(merge(
		[][]int{
			{1, 3}, {2, 6}, {8, 10}, {15, 18},
		},
	)) // expected [[1,6],[8,10],[15,18]]
}

func merge(intervals [][]int) [][]int {
	var merged [][]int

	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	for _, interval := range intervals {
		length := len(merged)
		if len(merged) == 0 || merged[length-1][1] < interval[0] {
			merged = append(merged, interval)
		} else {
			merged[length-1][1] = max(
				merged[length-1][1],
				interval[1],
			)
		}
	}

	return merged
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
