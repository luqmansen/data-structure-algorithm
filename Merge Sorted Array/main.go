package main

import (
	"fmt"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	nums1 = nums1[:m]

	for _, v := range nums2 {
		nums1 = append(nums1, v)
	}

	for range nums1 {
		for idx, val := range nums1 {
			if idx != 0 {
				if val > nums1[idx-1] {
					nums1[idx] = nums1[idx-1]
					nums1[idx-1] = val
				}

			}
		}
	}
	var newArr []int
	for idx, _ := range nums1 {
		newArr = append(newArr, nums1[len(nums1)-1-idx])
	}

	copy(nums1, newArr)
}

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	nums2 := []int{2, 5, 6}
	merge(nums1, 3, nums2, 3)
	fmt.Println(nums1)
}
