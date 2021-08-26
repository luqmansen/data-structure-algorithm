package main

import (
	"fmt"
	"sort"
)

func subsetA(arr []int) []int {
	sort.Sort(sort.Reverse(sort.IntSlice(arr)))
	i := 0
	j := 0
	allSubsetA := make([][]int, 0)
	// 5 4 3 2 1
	for j < len(arr)-1 {
		subsetA := arr[i : j+2]
		//hack stuff to skip few last array
		if j >= len(arr)-len(arr)/3 {
			j++
			continue
		}
		subsetB := arr[j+2:]
		subsetB = append(subsetB, arr[:i]...)
		fmt.Println(subsetA, subsetB)
		if len(subsetA) < len(subsetB) {
			if AbiggerThanB(subsetA, subsetB) {
				allSubsetA = append(allSubsetA, subsetA)
			}
			j += 2
		} else {
			i++
		}

	}
	fmt.Println(allSubsetA[0])
	if len(allSubsetA) > 0 {
		sort.Ints(allSubsetA[0])
		return allSubsetA[0]
	}
	return []int{}

}

func AbiggerThanB(arrA, arrB []int) bool {
	var sumA int
	var sumB int

	for idx, _ := range arrB {
		sumB += arrB[idx]
		if idx < len(arrA) {
			sumA += arrA[idx]
		}
	}
	return sumA > sumB
}

func main() {
	//arr := []int{3,7,5,6,2}
	//arr := []int{5,3,2,4,1,2}
	arr := []int{5, 4, 3, 2, 1, 0}
	//arr := []int{2,	3,	4,	4,	5,	9,	7,	8,	6,	10,	4,	5,	10,	10,	8,	4,	6,	4,	10,	1}
	fmt.Println(subsetA(arr))
}
