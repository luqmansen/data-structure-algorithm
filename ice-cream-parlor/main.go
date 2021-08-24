package main

import (
	"fmt"
)

/*
 * Complete the 'whatFlavors' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY cost
 *  2. INTEGER money
 */

//https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
func whatFlavors(cost []int32, money int32) {

	// money = 5
	costDict := make(map[int32]int)
	for idx, val := range cost {
		costDict[val] = idx
	}

	for idx, val := range cost {
		toFind := money - val
		if idx2, found := costDict[toFind]; found {
			if idx2 != idx {
				fmt.Println(idx+1, idx2+1)
				break
			}
		}

	}
}

func main() {
	test1 := []int32{4, 3, 2, 5, 7}
	whatFlavors(test1, 8)
}
