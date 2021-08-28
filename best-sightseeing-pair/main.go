package main

// O(N^2) solution
func maxScoreSightseeingPair2(values []int) int {

	maxNum := 0

	for i := 0; i < len(values); i++ {
		for j := i; j < len(values); j++ {
			if i != j {

				calc := values[i] + values[j] + i - j
				// fmt.Println(values[i], " +" , values[j], " + ",i,  " - ", j, " = ", calc   )
				maxNum = Max(maxNum, calc)
			}
		}
	}
	return maxNum
}

// from discussion, O(N)
func maxScoreSightseeingPair(values []int) int {

	// reform the formula to (values[i] + i) + (values[j] - j )
	maxPrev := values[0] + 0
	answ := 0

	// i start from 1 since prev is start from 0
	for i := 1; i < len(values); i++ {
		answ = Max(answ, maxPrev+values[i]-i)
		maxPrev = Max(maxPrev, values[i]+i)
	}
	return answ
}

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
