package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {

	input := "1.345.679"
	input = strings.Replace(input, ".", "", -1)

	for pos, char := range input {
		ch := string(char)
		x, _ := strconv.Atoi(ch)
		out := float64(x) * math.Pow(10, float64(len(input)-1-pos))
		fmt.Printf("%v\n", int(out))
	}

}
