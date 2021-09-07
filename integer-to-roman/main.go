package main

import (
	"fmt"
	"strings"
)

func intToRoman(num int) string {
	// 122 100 10x2 2
	//
	// C   XX   II
	// 129 100 10x2 10-1
	//

	sym := map[int]string{
		1:    "I",
		4:    "IV",
		5:    "V",
		9:    "IX",
		10:   "X",
		40:   "XL",
		50:   "L",
		90:   "XC",
		100:  "C",
		400:  "CD",
		500:  "D",
		900:  "CM",
		1000: "M",
	}
	// 3999
	unit := num % 10                         // 9
	dozen := num%100 - unit                  // 90
	hundred := num%1000 - dozen - unit       // 900
	thousand := num - hundred - dozen - unit // 3000

	res := make([]string, 0)

	roman := ""
	if unit < 4 {
		for i := 0; i < unit; i++ {
			roman += "I"
		}
	} else if unit > 5 && unit < 9 {
		roman = "V"
		for i := 0; i < unit-5; i++ {
			roman += "I"
		}
	} else if unit != 0 {
		roman = sym[unit]
	}

	res = append(res, roman)

	if dozen != 0 {
		roman = ""
		if dozen < 40 {
			for i := 0; i < dozen/10; i++ {
				roman += "X"
			}
		} else if dozen > 50 && dozen < 90 {
			roman = "L"
			for i := 0; i < dozen/10-5; i++ {
				roman += "X"
			}
		} else {
			roman = sym[dozen]
		}
		res = append(res, roman)
	}
	if hundred != 0 {
		roman = ""
		if hundred > 100 && hundred < 400 {
			for i := 0; i < hundred/100; i++ {
				roman += "C"
			}
		} else if hundred > 500 && hundred < 900 {
			roman = "D"
			for i := 0; i < hundred/100-5; i++ {
				roman += "C"
			}
		} else {
			roman = sym[hundred]
		}
		res = append(res, roman)

	}

	if thousand != 0 {
		roman = ""
		for i := 0; i < thousand/1000; i++ {
			roman += "M"
		}

		res = append(res, roman)
	}

	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}

	return strings.Join(res, "")
}
func main() {
	//"M CM XC IV"
	// 1 9 9 4
	fmt.Println(intToRoman(200))
}
