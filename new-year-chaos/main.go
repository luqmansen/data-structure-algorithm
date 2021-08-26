package main

import (
	"fmt"
)

func minimumBribes(q []int32) {
	// 1 2 5  3  7 8 6 (4)
	// 1 2 3 (4) 5 6 7  8

	var bribeTime int
	for idx, Person := range q {

		if int(Person)-1-idx > 2 {
			fmt.Println("Too chaotic")
			return
		}

		for i := Max(0, Person-2); i <= int32(idx); i++ {
			if q[int(i)] > Person {
				bribeTime += 1
			}
		}
	}
	fmt.Println(bribeTime)
}

func Max(x, y int32) int32 {
	if x < y {
		return y
	}
	return x
}

func main() {
	minimumBribes([]int32{1, 2, 5, 3, 7, 8, 6, 4})
}
