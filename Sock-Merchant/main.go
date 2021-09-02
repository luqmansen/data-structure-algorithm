package main

import (
	"fmt"
)

func matchSock(n int, ar []int) int {

	var pair int
	sockPair := make(map[int]int)

	for _, val := range ar {
		if _, ok := sockPair[val]; ok {
			sockPair[val] += 1
		} else {
			sockPair[val] = 1
		}
	}
	fmt.Println(sockPair)

	for _, value := range sockPair {
		if value >= 2 {
			if value%2 == 1 {
				pair += (value - 1) / 2
			} else {
				pair += value / 2
			}
		} else {
			continue
		}
	}

	return pair
}
