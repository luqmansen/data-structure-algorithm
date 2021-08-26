package utils

import (
	sort "sort"
	"strings"
)

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func ListToSet(input []string) []string {
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

func isAnagram(a, b string) bool {

	m := strings.Split(a, "")
	n := strings.Split(b, "")

	sort.Strings(m)
	sort.Strings(n)

	if strings.Join(m, "") == strings.Join(n, "") {
		return true
	}
	return false
}
