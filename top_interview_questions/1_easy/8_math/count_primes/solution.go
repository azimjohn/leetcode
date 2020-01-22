package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(countPrimes(10)) // expected 4
}

func countPrimes(n int) int {
	var primes []int
	numbers := make(map[int]bool)

	for i := 2; i < n; i++ {
		numbers[i] = true
	}

	for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}

	for _, prime := range primes {
		for i := prime * prime; i < n; i += prime {
			if i%prime == 0 {
				numbers[i] = false
			}
		}
	}

	total := 0
	for _, prime := range numbers {
		if prime {
			total++
		}
	}

	return total
}

func isPrime(n int) bool {
	if n == 2 {
		return true
	}

	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}
