package main

import (
	"fmt"
	"strings"
)

func romanToInt(s string) int {

	str := strings.Split(s, "")

	sym := map[string]int{
		"I":  1,
		"IV": 4,
		"V":  5,
		"IX": 9,
		"X":  10,
		"XL": 40,
		"L":  50,
		"XC": 90,
		"C":  100,
		"CD": 400,
		"D":  500,
		"CM": 900,
		"M":  1000,
	}

	var numSplit []int
	fmt.Println(str)
	i := len(str) - 1
	for i >= 0 {
		if i != 0 {
			char := strings.Join(str[i-1:i+1], "")
			if val, found := sym[char]; found {
				numSplit = append(numSplit, val)
				i -= 2
				continue
			}
		}

		if i >= 2 {
			if str[i] == str[i-1] && str[i-1] == str[i-2] {
				numSplit = append(numSplit, sym[str[i]]+sym[str[i-1]]+sym[str[i-2]])
				i -= 3
				continue
			}
		} else if i >= 1 {
			if str[i] == str[i-1] {
				numSplit = append(numSplit, sym[str[i]]+sym[str[i-1]])
				i -= 2
				continue
			}
		}
		numSplit = append(numSplit, sym[str[i]])
		i--
	}
	res := 0
	for _, val := range numSplit {
		res += val
	}
	return res
}

func main() {

	//romanToInt("III")
	romanToInt("LVIII")
	//romanToInt("MCMXCIV")
}
