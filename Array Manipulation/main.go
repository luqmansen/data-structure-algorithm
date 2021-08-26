package main

import (
	"fmt"
	"sort"
)

// Complete the arrayManipulation function below.

func arrayManipulation(n int, queries [][]int) int {

	arr := make([]int, n)

	for j := 0; j < len(queries); j++ {
		for k := queries[j][0] - 1; k <= queries[j][1]-1; k++ {
			arr[k] += queries[j][2]
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(arr)))
	return arr[0]
}

func arrayManipulation2(n int, queries [][]int) int {

	arr := make([]int, n+2)

	for j := 0; j < len(queries); j++ {

		arr[queries[j][0]] += queries[j][2]
		arr[(queries[j][1])+1] -= queries[j][2]

	}
	for i := 1; i < len(arr); i++ {
		arr[i] += arr[i-1]
	}
	sort.Slice(arr, func(i, j int) bool {
		return arr[i] > arr[j]
	})
	return arr[0]

}

// Trying to solve this again
func arrayManipulation3(n int, queries [][]int) int {

	resArr := make([]int, 2*n)

	//    a b k    a b k     a b k
	// [ [1,2,3], [4,5,6],  [7,8,9]]

	for _, innerArr := range queries {
		a := innerArr[0]
		b := innerArr[1]
		k := innerArr[2]

		resArr[a-1] += k
		resArr[b] -= k

		fmt.Println(resArr)

	}
	var maxSum int
	var arrSum int
	sort.Sort(sort.Reverse(sort.IntSlice(resArr)))

	fmt.Println(resArr)
	for _, val := range resArr {
		arrSum += val
		maxSum = Max(maxSum, arrSum)
	}
	return maxSum
}

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func main() {
	q := [][]int{{1, 5, 3}, {4, 8, 7}, {6, 9, 1}}
	//q := [][]int{{1, 2, 100}, {2, 5, 100}, {3, 4, 100}}
	//q := [][]int{{2, 6, 8}, {3,5, 7}, {1,8,1}, {5,9,15}}
	x := arrayManipulation3(5, q)
	fmt.Println(x)
}
