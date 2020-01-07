import "math/rand"

type RandomizedSet struct {
	hashMap map[int]int
	list    []int
}


/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{map[int]int{}, []int{}}
}


/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (r *RandomizedSet) Insert(val int) bool {
	_, exists := r.hashMap[val]
	if !exists {
		r.hashMap[val] = len(r.list)
		r.list = append(r.list, val)

		return true
	}
	return false
}


/** Removes a value from the set. Returns true if the set contained the specified element. */
func (r *RandomizedSet) Remove(val int) bool {
	index, exists := r.hashMap[val]
	if exists {
		length := len(r.list)

		delete(r.hashMap, val)
		r.list[index] = r.list[length-1]
		lastVal := r.list[length-1]
		r.list = r.list[:length-1] // pop - O(1) ?

		if val != lastVal{
			r.hashMap[lastVal] = index
		}

		return true
	}
	return false
}


/** Get a random element from the set. */
func (r *RandomizedSet) GetRandom() int {
	length := len(r.list)
	return r.list[rand.Intn(length)]
}
