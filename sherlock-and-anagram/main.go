package main

import (
	"fmt"
	"sort"
	"strings"
)

func sherlockAndAnagrams(s string) int32 {
	split := strings.Split(s, "")
	// [a,b,b,c]
	//  0 1 2 3
	substrList := make([]string, 0)

	for i := 0; i < len(split); i++ {
		// a
		for j := i + 1; j <= len(split); j++ {
			substr := split[i:j]
			//sort.Strings(substr)
			sorted := strings.Join(substr, "")
			substrList = append(substrList, sorted)
		}
	}

	substrCnt := make(map[string]int)
	for _, substr := range substrList {
		if _, found := substrCnt[substr]; found {
			substrCnt[substr] += 1
		} else {
			substrCnt[substr] = 1
		}
	}

	substrCntUpdate := make(map[string]int)
	for k, v := range substrCnt {
		splited := strings.Split(k, "")
		sort.Strings(splited)
		splitedJoin := strings.Join(splited, "")
		substrCntUpdate[splitedJoin] += v
	}
	fmt.Println(substrCntUpdate)

	anagramCnt := 0
	for _, v := range substrCntUpdate {
		if v > 1 {
			if v > 2 {
				anagramCnt += v
			} else {
				anagramCnt++
			}
		}
	}
	return int32(anagramCnt)
}

func main() {
	fmt.Println(sherlockAndAnagrams("abba"))

}
