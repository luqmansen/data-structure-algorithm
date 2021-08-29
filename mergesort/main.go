package main

import "fmt"

func mergeSortedArray(arr1, arr2 []int) []int {

	len1 := len(arr1)
	len2 := len(arr2)

	//allocate for new sorted array
	arr3 := make([]int, len1+len2)

	ptr1, ptr2, ptr3 := 0, 0, 0 // pointer for index

	for ptr1 < len1 && ptr2 < len2 {

		if arr1[ptr1] < arr2[ptr2] {
			arr3[ptr3] = arr1[ptr1]
			ptr1++
			ptr3++
		} else {
			arr3[ptr3] = arr2[ptr2]
			ptr2++
			ptr3++
		}
	}
	// when one of the pointer reach end of index (len(arr) + 1)
	// copy left over item on the arr1 or arr2 to arr3
	for ptr1 < len1 {
		arr3[ptr3] = arr1[ptr1]
		ptr3++
		ptr1++
	}

	for ptr2 < len2 {
		arr3[ptr3] = arr2[ptr2]
		ptr2++
		ptr3++
	}

	return arr3
}

func mergesort(arr []int) {
	if len(arr) > 1 {

		mid := len(arr) / 2

		left := arr[:mid]

		right := arr[mid:]

		mergesort(left)
		mergesort(right)

		copy(arr, mergeSortedArray(left, right))
	}
}

func main() {
	t := []int{7, 4, 3, 2, 1, 5, 6}
	mergesort(t)
	fmt.Println(t)
}
