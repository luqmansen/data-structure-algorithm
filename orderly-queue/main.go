package main

import (
	"fmt"
	"sort"
	"strings"
)

func orderlyQueue(str string, k int) string {
	s := strings.Split(str, "")

	if k == 1 {
		var res []string
		for i := 0; i <= len(s); i++ {
			a := s[i:]
			b := s[:i]

			res = append(res, strings.Join(append(a, b...), ""))
		}
		sort.Slice(res, func(i, j int) bool {
			return res[i] < res[j]
		})
		return res[0]
	}
	// k=1
	//cba > bac > acb > cba
	//

	sort.Slice(s, func(i, j int) bool {
		return s[i] < s[j]
	})
	return strings.Join(s, "")
}

func main() {
	fmt.Println(orderlyQueue("cba", 1))
	//fmt.Println(orderlyQueue("nhtq",1)) //h t q n
}
