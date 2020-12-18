package main

import "fmt"

func sortedSquares(nums []int) []int {
	for i, v := range nums {
		nums[i] = v * v
	}
	for range nums {
		for idx, val := range nums {
			if idx != 0 {
				if val > nums[idx-1] {
					nums[idx] = nums[idx-1]
					nums[idx-1] = val
				}

			}
		}
	}

	var newArr []int
	for idx, _ := range nums {
		newArr = append(newArr, nums[len(nums)-1-idx])
	}

	fmt.Println(newArr)
	return newArr
}

func main() {
	arr := []int{-7, -3, 2, 3, 11}
	sortedSquares(arr)
}
