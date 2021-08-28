package main

import (
	"fmt"
	"sort"
)

func arrayRankTransform(arr []int) []int {

	temp := make([]int, len(arr))

	copy(temp, arr)

	sort.Ints(temp)
	fmt.Println(temp)

	dict := make(map[int]int) //  {value:index}
	incr := 0
	for idx, val := range temp {
		if _, found := dict[val]; !found {
			dict[val] = idx + 1 + incr
		} else {
			incr--
		}
	}
	fmt.Println(dict)
	for idx, val := range arr {
		rank := dict[val]
		fmt.Println(val, " ", rank)
		arr[idx] = rank

	}
	fmt.Println(arr)

	return arr

}

func main() {
	arrayRankTransform([]int{37, 12, 28, 9, 100, 56, 80, 5, 12})
	//[6 3 5 2 9 7 8 1 3]
	//[5,3,4,2,8,6,7,1,3]
}
