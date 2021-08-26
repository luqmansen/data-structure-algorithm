package main

import "fmt"

//https://www.hackerrank.com/challenges/minimum-swaps-2/problem
func minimumSwaps(oldArr []int32) int32 {

	arr := make([]int, len(oldArr))
	for idx, val := range oldArr {
		arr[idx] = int(val)
	}

	a := make(map[int]int, len(arr))
	b := make(map[int]int, len(arr))

	for idx, val := range arr {
		a[idx] = val - 1
		b[val-1] = idx
	}
	// [3 ,2 ,0  ,1]
	//A{0: 3, 1: 2, 2: 0, 3: 1} index : value
	//A{0: 3, 1: 0, 2: 2, 3: 1} index : value
	//=======================
	//B{3: 0, 2: 1, 0: 2, 1: 3} value : index
	//B{3: 0, 2: 2, 0: 1, 1: 3} value : index
	var swap int32
	for idx, val := range a { // idx 2, val 0
		if idx != val {
			idxOfCorrectVal := b[idx] // cari lokasi index dari value Val di dict B (cari by value)
			a[idxOfCorrectVal] = val
			a[idx] = idx

			b[val] = idxOfCorrectVal
			b[idx] = idx

			swap++
		}
	}
	return swap
}

func main() {
	arr := []int32{4, 3, 1, 2} // 3, 2, 0 ,1
	fmt.Println(minimumSwaps(arr))
}
