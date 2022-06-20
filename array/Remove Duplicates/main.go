package main

import "fmt"

func removeDuplicates(nums []int) int {
	//1,1,2,2,3
	//1,1,2,2,3
	var i int
	for j := 1; j < len(nums); j++ {
		if nums[j] != nums[i] {
			i++
			nums[i] = nums[j]
		}
	}
	return i + 1
}
func main() {
	arr := []int{1, 1, 2, 2, 3}
	res := removeDuplicates(arr)
	fmt.Println(arr)
	fmt.Println(res)
}
