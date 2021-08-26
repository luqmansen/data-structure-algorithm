package main

import (
	"fmt"
	"strings"
)

// O(n^3) solution
func lengthOfLongestSubstring1(s string) int {
	split := strings.Split(s, "")
	maxLen := 0

	for i := 0; i < len(split); i++ {
		for j := i + 1; j <= len(split); j++ {
			substr := split[i:j]
			substrLen := len(substr)
			if substrLen == len(listToSet(substr)) {
				maxLen = Max(maxLen, substrLen)
			}
		}
	}

	return maxLen
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func listToSet(input []string) []string {
	sets := make(map[string]bool, 0)
	output := make([]string, 0)

	for _, val := range input {
		if _, found := sets[val]; !found {
			sets[val] = true
			output = append(output, val)
		}
	}
	return output
}

func main() {
	fmt.Print(lengthOfLongestSubstring1("abcabcbb"))
}
