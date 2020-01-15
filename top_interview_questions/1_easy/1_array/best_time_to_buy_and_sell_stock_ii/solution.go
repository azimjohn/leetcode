package main

import "fmt"

func main() {
	fmt.Println(maxProfit([]int{1, 2, 3, 4, 5})) // expected 4
}

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}

	minPrice, maxPrice := prices[0], prices[0]
	totalGain, currentGain := 0, 0

	for _, price := range prices[1:] {
		if price < maxPrice {
			currentGain = maxPrice - minPrice
			totalGain += currentGain
			minPrice = price
		}
		maxPrice = price
	}

	currentGain = maxPrice - minPrice
	totalGain += currentGain

	return totalGain
}
