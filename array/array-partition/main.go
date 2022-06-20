package main

import (
	"fmt"
	"sort"
)

func solve(arr []int) int {
	sort.Sort(sort.Reverse(sort.IntSlice(arr)))
	subsetGcdIsOne := 0

	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr); j++ {
			if i < j {
				subsetA := arr[i:j]
				fmt.Println(subsetA)
			}
		}
	}

	return subsetGcdIsOne

}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func main() {
	solve([]int{3, 2, 1, 0})
}
