package main

func main() {

}

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}

	maxVal, minVal := prices[0], prices[0]
	maxGain, currGain := 0, 0

	for _, price := range prices[1:] {
		if price > maxVal {
			maxVal = price
			currGain = maxVal - minVal
			if currGain > maxGain {
				maxGain = currGain
			}
		}

		if price < minVal {
			minVal = price
			maxVal = price
			currGain = 0
		}
	}

	return maxGain
}
