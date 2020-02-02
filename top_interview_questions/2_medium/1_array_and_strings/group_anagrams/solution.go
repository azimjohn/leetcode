package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
	/* Expected
	[
	  ["ate","eat","tea"],
	  ["nat","tan"],
	  ["bat"]
	]
	*/
}

func groupAnagrams(strs []string) [][]string {
	var key string
	var groups [][]string
	hashMap := make(map[string][]string)

	for _, str := range strs {
		key = anagramKey(str)
		hashMap[key] = append(hashMap[key], str)
	}

	for _, v := range hashMap {
		groups = append(groups, v)
	}

	return groups
}

func anagramKey(s string) string {
	r := []byte(s)

	sort.Slice(r, func(i, j int) bool {
		return r[i] < r[j]
	})

	return string(r)
}
