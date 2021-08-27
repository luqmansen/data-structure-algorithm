package main

import "fmt"

func main() {
	// arr = a b c d e f g h i
	//       0 1 2 3 4 5 6 7 8
	// remove 1 3 5 7 (len = 4)
	//		  b d f h
	//        0 1 2 3
	// arr[:1] + arr[1:3] + arr [3:5] + arr[5:7] + arr[7:]
	// result = a c e g i
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
	left := 0
	right := len(arr) - 1

	fmt.Println(binarySearch(arr, left, right, 14))

}

func binarySearch(arr []int, left, right, find int) int {

	for left <= right {
		mid := left + ((right - left) / 2)

		if arr[mid] == find {
			return mid
		}
		//arr := []int{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14}
		//                           ^

		if arr[mid] < find {
			left = mid + 1

		} else {
			right = mid - 1
		}
	}
	return -1
}
