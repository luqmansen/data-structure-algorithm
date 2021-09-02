package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {

	input := "1.345.679.653.123.134.123"

	outputNumber(input)

}

func outputNumber(s string) {
	s = strings.Replace(s, ".", "", -1)
	for pos, char := range s {
		ch := string(char)
		x, _ := strconv.Atoi(ch)
		multiplier := math.Pow(10, float64(len(s)-1-pos))
		out := float64(x) * multiplier
		fmt.Printf("%v\n", int64(out))
	}
}
