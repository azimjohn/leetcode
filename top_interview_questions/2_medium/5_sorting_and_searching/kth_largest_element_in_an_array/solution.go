package main

func main() {

}

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func findKthLargest(nums []int, k int) int {
	h := IntHeap{}
	copy(h, nums)
	// heap.Fix(h)
	// heap.Pop() // k-1 times
	// return head.Pop()

	return 0
}
