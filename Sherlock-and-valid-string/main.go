package main

import (
	"fmt"
	"strings"
)

//https://www.hackerrank.com/challenges/sherlock-and-valid-string/
func isValid(s string) string {
	splitString := strings.Split(s, "")

	stringChar := make(map[string]int)
	for _, char := range splitString {
		if _, found := stringChar[char]; found {
			stringChar[char] = stringChar[char] + 1
		} else {
			stringChar[char] += 1
		}

	}
	fmt.Println(stringChar)

	appearCount := make(map[int]int)
	for _, appearNum := range stringChar {
		if _, found := appearCount[appearNum]; found {
			appearCount[appearNum] = appearCount[appearNum] + 1
		} else {
			appearCount[appearNum] += 1
		}
	}
	if len(appearCount) > 2 {
		return "NO"
	}

	// {2:5, 1:4} NO
	// map[a:2 b:2 c:2 d:2 e:3 f:2 g:2 h:2]
	// {2:7, 3:1}
	//map[a:4 b:2 c:2]
	// {4:1, 2:2}
	firstKeyCount := 0
	firstKey := 0
	for key, num := range appearCount {
		if firstKeyCount == 0 {
			firstKeyCount = num
			firstKey = key
		} else {
			if firstKey-key > 1 {
				return "NO"
			}
			if firstKeyCount > 1 && num > 1 {
				return "NO"
			}
		}

	}
	return "YES"

}

func main() {
	fmt.Println(isValid("aaaabbcc"))
}
