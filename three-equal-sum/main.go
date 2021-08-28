package main

import (
	"fmt"
	"sort"
)

func canThreePartsEqualSum(arr []int) bool {
	total := sumArray(arr)
	k := 3
	if total%k != 0 {
		return false
	}
	targetBucketSum := total / k

	used := make([]bool, len(arr))

	return canPartition(0, arr, used, k, 0, targetBucketSum)
}

func canPartition(iterationStart int, arr []int, used []bool, k int, progressBucketSum int, targetSum int) bool {
	//fmt.Println(k , " ", progressBucketSum)
	if k == 1 {
		return true
	}

	if progressBucketSum > targetSum {
		return false
	}

	if progressBucketSum == targetSum {
		return canPartition(0, arr, used, k-1, 0, targetSum)
	}

	for i := iterationStart; i < len(arr); i++ {
		if used[i] == false {
			used[i] = true
			if canPartition(i+1, arr, used, k, progressBucketSum+arr[i], targetSum) {
				return true
			}
			used[i] = false
		}
	}
	return false
}

func sumArray(arr []int) int {
	var sum int
	for _, val := range arr {
		sum += val
	}
	return sum
}

func main() {
	//arr := []int{3,3,6,5,-2,2,5,1,-9,4}
	//arr := []int{0,2,1,-6,6,7,9,-1,2,0,1}
	arr := []int{0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1}
	fmt.Println(sumArray(arr))

	sort.Ints(arr)
	fmt.Println(arr)

	fmt.Println(canThreePartsEqualSum(arr))
}
