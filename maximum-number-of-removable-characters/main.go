package main

import (
	"fmt"
	"github.com/luqmansen/data-structure-algorithm/utils"
	"sort"
	"strings"
)

// logN * N^2
func maximumRemovals(s string, p string, removable []int) int {

	var maxRemoved int
	subSeqSplit := strings.Split(p, "")

	left := 0
	right := len(removable) - 1

	// binary search
	for left <= right {

		mid := left + ((right - left) / 2)

		idxToRemove := removable[:mid+1]
		seqString := strings.Split(s, "")
		newString := removeItemInArr2(seqString, idxToRemove) // O(n)
		if IsSubSequence(subSeqSplit, newString) == true {    // O(n)
			left = mid + 1
			maxRemoved = utils.Max(maxRemoved, len(idxToRemove))
		} else {
			right = mid - 1
		}
	}

	return maxRemoved
}

// original solution, too complex lol
func removeItemInArr(arr []string, idxs []int) []string {
	// arr = a b c d e f g h i
	//       0 1 2 3 4 5 6 7 8
	// remove 1 3 5 7 (len = 4)
	//        0 1 2 3
	// arr[:1] + arr[1+1:3] + arr [3+1:5] + arr[5+1:7] + arr[7+1:]
	newIdxs := make([]int, len(idxs))
	copy(newIdxs, idxs)
	sort.Ints(newIdxs)

	result := make([]string, 0)
	for idx, toRemove := range newIdxs {

		if idx == 0 {
			leftover := arr[:toRemove]
			result = append(result, leftover...)
		} else {
			upperBound := newIdxs[idx-1] + 1
			leftover := arr[upperBound:toRemove]
			result = append(result, leftover...)
		}
		if idx == len(newIdxs)-1 {
			leftover := arr[toRemove+1:]
			result = append(result, leftover...)
		}
	}

	return result
}

// from discussion
func removeItemInArr2(newArr []string, idxs []int) []string {

	for _, idxToRemove := range idxs {
		newArr[idxToRemove] = ""
	}

	s := strings.Join(newArr, "")
	return strings.Split(s, "")
}

// time complexity O(n)
func IsSubSequence(subSeq, seq []string) bool {

	subLen := len(subSeq)
	seqLen := len(seq)
	subPointer := 0

	for i := 0; i < seqLen && subPointer < subLen; i++ {
		if subSeq[subPointer] == seq[i] {
			subPointer++
		}
	}
	return subPointer == subLen
}

func main() {

	s := "abcbddddd"
	p := "abcd"

	remove := []int{3, 2, 1, 4, 5, 6}

	res := maximumRemovals(s, p, remove)
	fmt.Println(res)

}
