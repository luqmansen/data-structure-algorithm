package main

import (
	"fmt"
	"github.com/luqmansen/data-structure-algorithm/utils"
	"sort"
)

// 621 ms 10MB memory usage
func merge1(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	i := 0 // first array
	j := 1 // second array
	for i < len(intervals) {

		A := intervals[i]
		var B []int
		if j < len(intervals) {
			B = intervals[j]
		} else {
			break
		}
		if A[1] > B[0] || A[1] == B[0] || B[0] < A[0] {
			// merge
			merged := mergeArr(A, B)
			prev := intervals[:i]
			next := intervals[j+1:]
			intervals = nil
			intervals = append(intervals, prev...)
			intervals = append(intervals, merged)
			intervals = append(intervals, next...)
		} else {
			i++
			j++

		}

	}
	return intervals
}

func mergeArr(a, b []int) []int {
	res := make([]int, 0)
	res = append(res, a...)
	res = append(res, b...)
	sort.Ints(res)
	return []int{res[0], res[3]}
}

// approach 2
// not actually merge the array
// src https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/intervalmerging
func merge(intervals [][]int) [][]int {

	if len(intervals) == 0 {
		return intervals
	}

	// sort ascending
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	res := make([][]int, 0)
	res = append(res, intervals[0])

	for i := 1; i < len(intervals); i++ {

		curr := intervals[i]
		last := res[len(res)-1]

		if curr[0] <= last[1] {
			last[1] = utils.Max(last[1], curr[1])
		} else {
			res = append(res, curr)
		}
	}

	return res

}

func main() {
	//intervals := [][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}}
	//intervals := [][]int{{1, 4}, {4, 5}}
	//intervals := [][]int{{1, 4}, {0, 4}}
	intervals := [][]int{{1, 4}, {0, 0}}

	fmt.Println(merge(intervals))
}
