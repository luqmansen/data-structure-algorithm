package main

import "fmt"

func duplicateZeros(arr []int) {
	arrLen := len(arr) - 1
	var currIdx int
	for range arr {
		if currIdx <= arrLen {
			if arr[currIdx] == 0 {
				for i := arrLen; i >= currIdx+1; i-- {
					if i+1 <= arrLen {
						arr[i+1] = arr[i]
					}
				}
				if currIdx < arrLen {
					arr[currIdx+1] = 0
				}

				currIdx++ // skip after added 0
			}
		}
		currIdx++
	}
}

func main() {
	arr := []int{1, 0, 2, 3, 0, 4, 5, 0}
	fmt.Println(arr)
	duplicateZeros(arr)
	fmt.Println(arr)

}
