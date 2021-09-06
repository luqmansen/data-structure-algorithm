package main

import (
	"fmt"
	"strings"
)

func convert(s string, numRows int) string {

	/*
		PAYPALISHIRING
		row = 3
		0[P   A   H   N]
		1[A P L S I I G]
		2[Y   I   R]
		PAHN APLSIIG YIR

		arrr[
		[] 0
		[] 1
		[] 2
		]
	*/
	if numRows == 1 {
		return s
	}
	str := strings.Split(s, "")

	arr := make([][]string, numRows)
	i := 0
	operator := "+"
	for _, c := range str {
		arr[i] = append(arr[i], c)
		if operator == "+" {
			i++
		} else {
			i--
		}
		if i == numRows-1 || i == 0 {
			if operator == "+" {
				operator = "-"
			} else {
				operator = "+"
			}
		}
	}
	var res []string
	for _, ar := range arr {
		res = append(res, strings.Join(ar, ""))
	}

	return strings.Join(res, "")
}

func main() {
	fmt.Println(convert("AB", 1))
}
