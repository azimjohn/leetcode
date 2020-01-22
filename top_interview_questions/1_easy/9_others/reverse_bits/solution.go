package main

func main() {
}

func reverseBits(num uint32) uint32 {
	var reversed uint32 = 0

	for i := 0; i < 32; i++ {
		lastDigit := num & 1
		reversed = reversed << 1
		reversed += lastDigit
		num = num >> 1
	}

	return reversed
}
