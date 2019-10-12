package main

import "fmt"

func WalkingLamp(n int, lamp []bool) int {
	var count int
	init := 1
	for i := 0; i < n; i++ {
		for idx, _ := range lamp {
			if (idx+1)%init == 0 {
				lamp[idx] = !lamp[idx]
			}
		}
		init++
	}

	fmt.Println(lamp)
	for _, val := range lamp{
		if val == true{
			count++
		}
	}
	return count
}

func main() {

	lamp := make([]bool, 10)
	trip := 3

	fmt.Println(WalkingLamp(trip, lamp))

}
