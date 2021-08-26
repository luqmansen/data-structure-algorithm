package main

import (
	"fmt"
)

func leftRotation(arr []int32, d int) []int32 {

	if len(arr) == d {
		return arr
	} else {
		for i := 0; i < d; i++ {
			temp := arr[0]
			for j := 0; j < len(arr)-1; j++ {
				arr[j] = arr[j+1]
			}
			arr[len(arr)-1] = temp
		}
	}
	return arr
}

func rotLeft(arr []int32, d int32) []int32 {
	if len(arr) == int(d) {
		return arr
	} else {
		newArr := make([]int32, len(arr))
		for idx, _ := range arr {
			newIdx := (idx + (len(arr) - int(d))) % len(arr)
			newArr[newIdx] = arr[idx]
		}
		return newArr
	}
}

func main() {
	test := []int32{1, 2, 3, 4}
	//0, 1, 2, 3
	fmt.Println(rotLeft(test, 1))

}
